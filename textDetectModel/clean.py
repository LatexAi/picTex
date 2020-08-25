import cv2
from scipy.optimize import curve_fit, minimize
import numpy as np
import collections
from PIL import Image

def getAvgWhite(img_bw, debug=True):
    total_pixel = sorted(img_bw.flatten())
    total_pixel = list(filter(lambda num: num != 0 and num != 255,
                              total_pixel))
    pixel_dict = collections.Counter(total_pixel)
    pixel_x = []
    hist_y = []

    for grey_scale_value in sorted(pixel_dict.keys()):
        pixel_x.append(grey_scale_value)
        hist_y.append(pixel_dict[grey_scale_value])

    def gauss(x, mu, sigma, A):
        return A * np.exp(-(x - mu) ** 2 / 2 / sigma ** 2)

    def bimodal(x, mu1, sigma1, A1, mu2, sigma2, A2):
        return gauss(x, mu1, sigma1, A1) + gauss(x, mu2, sigma2, A2)

    max_val = max(hist_y)

    expected = (130, 40, max_val, 170, 20, max_val)
    bounds = ([ 100.,   0.,      0., 150.,   0.,      0.],
              [ 250., 255., max_val, 255., 255., max_val])

    params, cov = curve_fit(bimodal, pixel_x, hist_y, expected,
                            bounds=bounds, maxfev=10800)
    func = lambda x: bimodal(x, *params)

    params = list(params)
    max_hump = params.index(max(params[1], params[4]))
    mean = params[max_hump-1]
    std  = params[max_hump]
    thresh_min = mean - 2*std
    thresh_max = mean + 2*std
    return thresh_min, thresh_max, mean, std

def convert(image, debug=False):
    """
    Remove the background.
        1. Convert the image to a black and white mask.
        2. Get the average pixel color
        2. Group the white pixel together and find the largest contour
    """

    img_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh_min, thresh_max, mean, std = getAvgWhite(img_bw)
    thresh_min = 0 if thresh_min < 0 else int(thresh_min)
    thresh_max = 255 if thresh_max > 255 else int(thresh_max)
    ret, img_bw_threshold = cv2.threshold(img_bw, thresh_min, thresh_max,
                                                  cv2.THRESH_BINARY)
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 8))
    img_bw_threshold = cv2.morphologyEx(img_bw_threshold, cv2.MORPH_CLOSE, k,
                            iterations=1)  # iter=2

    contours, hierarchy = cv2.findContours(
        img_bw_threshold, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE
    )

    max_area = 0
    max_page_bw = None
    max_page_color = None
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            x, y, w, h = cv2.boundingRect(cnt)
            max_page_bw = img_bw[y:y + h, x:x + w]
            max_page_color = image.copy()[y:y + h, x:x + w]
            max_page_bw = cv2.resize(max_page_bw, dsize=(1050, 1485),
                                     interpolation=cv2.INTER_LINEAR_EXACT)
            max_page_color = cv2.resize(max_page_color, dsize=(1050, 1485),
                                        interpolation=cv2.INTER_LINEAR_EXACT)


    thresh_min = mean - 4*std
    #print(thresh_min, mean, std)
    ret, img = cv2.threshold(max_page_bw, thresh_min, 255, cv2.THRESH_BINARY_INV)


    if debug:
        threshPIL = Image.fromarray(img)  # thresh
        threshPIL.show(title="threshold_image")

    return img



if __name__ == "__main__":
    urls = [
            "examples/IMG_7311.jpg",
        ]
    for url in urls:
        img = cv2.imread(url)  # local repository
        img = cv2.resize(img, dsize=(1050, 1485), interpolation=cv2.INTER_AREA)
        convert(img, debug=False)