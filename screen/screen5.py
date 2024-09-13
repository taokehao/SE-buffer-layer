import os
from mp_api.client import MPRester
import re
import warnings
from pymatgen.io.cif import CifWriter
import pandas as pd

warnings.filterwarnings("ignore")
# 使用 API key 初始化 MPRester
mpr = MPRester(api_key="RVtCSJCsgiKrM059ZGSaZVqPYgBoapvO")

# 加载数据
predict_df = pd.read_csv('./selected_materials.csv')
for i in predict_df['id']:
    mp_id = 'mp-' + str(i)
    if (mp_id=='mp-684024' or mp_id=='mp-559142' or mp_id=='mp-1019778' or mp_id=='mp-978840' or mp_id=='mp-6031' or mp_id=='mp-554324'
            or mp_id=='mp-14712' or mp_id=='mp-14871' or mp_id=='mp-1019609' or mp_id=='mp-1020705' or mp_id=='mp-1199122' or mp_id=='mp-532413'):
        continue
    print(mp_id)
    structure = mpr.get_structure_by_material_id(mp_id, conventional_unit_cell=True).add_oxidation_state_by_guess()  # conventional_unit_cell=True
    cif_writer = CifWriter(structure)  #symprec=0.01, refine_struct=True, write_site_properties=False
    cif_writer.write_file("./screen-data/" + mp_id[3:] + ".cif")
