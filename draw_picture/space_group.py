from mp_api.client import MPRester
import warnings
import pandas as pd
import numpy as np
warnings.filterwarnings("ignore")

mpr = MPRester(api_key="RVtCSJCsgiKrM059ZGSaZVqPYgBoapvO")

file_load = np.loadtxt('../data_load/id_list_all.txt', dtype=str)
crystal_system = []
space_group = []
count = 0
for i in file_load:
    count += 1
    mp_id = str(i)
    print(mp_id, count)
    docs = mpr.summary.search(material_ids=mp_id, fields=["symmetry"])[0]
    crystal_system.append(docs.symmetry.crystal_system)
    space_group.append(docs.symmetry.number)

file = open('./space_group_21686.txt', 'w')
for i in space_group:
    print(i, file=file)
file.close()

file = open('./crystal_system_21686.txt', 'w')
for i in crystal_system:
    print(i, file=file)
file.close()
