from mp_api.client import MPRester
import warnings
import pandas as pd
import numpy as np
warnings.filterwarnings("ignore")


elements_dict = {
    'H': 0, 'He': 0, 'Li': 0, 'Be': 0, 'B': 0, 'C': 0, 'N': 0, 'O': 0, 'F': 0, 'Ne': 0,
    'Na': 0, 'Mg': 0, 'Al': 0, 'Si': 0, 'P': 0, 'S': 0, 'Cl': 0, 'Ar': 0, 'K': 0, 'Ca': 0,
    'Sc': 0, 'Ti': 0, 'V': 0, 'Cr': 0, 'Mn': 0, 'Fe': 0, 'Co': 0, 'Ni': 0, 'Cu': 0, 'Zn': 0,
    'Ga': 0, 'Ge': 0, 'As': 0, 'Se': 0, 'Br': 0, 'Kr': 0, 'Rb': 0, 'Sr': 0, 'Y': 0, 'Zr': 0,
    'Nb': 0, 'Mo': 0, 'Tc': 0, 'Ru': 0, 'Rh': 0, 'Pd': 0, 'Ag': 0, 'Cd': 0, 'In': 0, 'Sn': 0,
    'Sb': 0, 'Te': 0, 'I': 0, 'Xe': 0, 'Cs': 0, 'Ba': 0, 'La': 0, 'Ce': 0, 'Pr': 0, 'Nd': 0,
    'Pm': 0, 'Sm': 0, 'Eu': 0, 'Gd': 0, 'Tb': 0, 'Dy': 0, 'Ho': 0, 'Er': 0, 'Tm': 0, 'Yb': 0,
    'Lu': 0, 'Hf': 0, 'Ta': 0, 'W': 0, 'Re': 0, 'Os': 0, 'Ir': 0, 'Pt': 0, 'Au': 0, 'Hg': 0,
    'Tl': 0, 'Pb': 0, 'Bi': 0, 'Po': 0, 'At': 0, 'Rn': 0, 'Fr': 0, 'Ra': 0, 'Ac': 0, 'Th': 0,
    'Pa': 0, 'U': 0, 'Np': 0, 'Pu': 0, 'Am': 0, 'Cm': 0, 'Bk': 0, 'Cf': 0, 'Es': 0, 'Fm': 0,
    'Md': 0, 'No': 0, 'Lr': 0, 'Rf': 0, 'Db': 0, 'Sg': 0, 'Bh': 0, 'Hs': 0, 'Mt': 0, 'Gs': 0,
    'Rg': 0, 'Cn': 0, 'Nh': 0, 'Fl': 0, 'Mc': 0, 'Lv': 0, 'Ts': 0, 'Og': 0, 'La-Lu': 0, 'Ac-Lr': 0
}
La_Lu = ['La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu']
Ac_Lr = ['Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']

nelements = []
for i in range(100):
    nelements.append(0)

nsites = []
for i in range(10000):
    nsites.append(0)

mpr = MPRester(api_key="RVtCSJCsgiKrM059ZGSaZVqPYgBoapvO")

file_load = np.loadtxt('../data_load/id_list_all.txt', dtype=str)
count = 0
for i in file_load:
    count += 1
    mp_id = str(i)
    print(mp_id, count)
    docs = mpr.summary.search(material_ids=mp_id, fields=["elements", "nelements", "nsites"])[0]
    nsites[docs.nsites] += 1
    nelements[docs.nelements] += 1
    for e in docs.elements:
        elements_dict[str(e)] += 1
        if elements_dict[str(e)] in La_Lu:
            elements_dict['La-Lu'] += 1
        if elements_dict[str(e)] in Ac_Lr:
            elements_dict['Ac-Lr'] += 1


file = open('./output/periodic-table-21686.txt', 'w')
for i in elements_dict:
    print(elements_dict[i], file=file)
file.close()


file = open('./output/nelements-21686.txt', 'w')
for i in nelements:
    print(i, file=file)
file.close()

file = open('./output/nsites-21686.txt', 'w')
for i in nsites:
    print(i, file=file)
file.close()
