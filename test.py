import os
import numpy as np
from mp_api.client import MPRester
import warnings
from pymatgen.io.cif import CifWriter
warnings.filterwarnings("ignore")

list = [6.8, 10.2, 13.6, 17, 20.4, 23.8, 27.2, 30.6, 34]
for i in list:
    label_list = open('./data_load/label_list.txt', 'r').readlines()
    out_list = []
    for label in label_list:
        band = float(label.strip('\n'))
        if band < i:
            out_list.append(0)
        else:
            out_list.append(1)
    print(out_list.count(0), out_list.count(1))


# file = open('./test.txt', 'w')
# for i in out_list:
#     print(i, file=file)
# file.close()
# 能带的分类标准是0.1
# 剪切模量的分类标准是27.2