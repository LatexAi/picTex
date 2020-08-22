# from collections import OrderedDict
# import numpy as np
# import torch
# import os
#
# data_dir = "./final/"
#
# classes = os.listdir(data_dir)
# num_classes = len(classes)
#
# classes_encode, classes_decode = {}, {}
# for i, name in enumerate(classes):
#     classes_encode[name] = i
#     classes_decode[i] = name
#
# encode_dict, decode_dict = OrderedDict(classes_encode), OrderedDict(classes_encode)
#
# classes = classes_decode

classes = {
 0: '(',
 1: ')',
 2: '+',
 3: '-',
 4: '0',
 5: '1',
 6: '2',
 7: '3',
 8: '4',
 9: '5',
 10: '6',
 11: '7',
 12: '8',
 13: '9',
 14: '=',
 15: 'a',
 16: 'alpha',
 17: 'ast',
 18: 'b',
 19: 'beta',
 20: 'c',
 21: 'comma',
 22: 'd',
 23: 'delta',
 24: 'e',
 25: 'emptyset',
 26: 'f',
 27: 'forall',
 28: 'full_stop',
 29: 'g',
 30: 'greater',
 31: 'h',
 32: 'implies',
 33: 'in',
 34: 'infty',
 35: 'int',
 36: 'j',
 37: 'k',
 38: 'l',
 39: 'lambda',
 40: 'land',
 41: 'leq',
 42: 'lesser',
 43: 'm',
 44: 'mu',
 45: 'n',
 46: 'nabla',
 47: 'Naturals',
 48: 'neq',
 49: 'o',
 50: 'p',
 51: 'perp',
 52: 'pi',
 53: 'q',
 54: 'r',
 55: 'Reals',
 56: 's',
 57: 'setminus',
 58: 'sigma',
 59: 'sim',
 60: 'sum',
 61: 'supset',
 62: 't',
 63: 'theta',
 64: 'u',
 65: 'v',
 66: 'varepsilon',
 67: 'w',
 68: 'x',
 69: 'y',
 70: 'z',
 71: '[',
 72: ']'}
