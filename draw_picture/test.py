from mp_api.client import MPRester
import warnings
from pymatgen.io.cif import CifWriter
import csv
warnings.filterwarnings("ignore")

# 使用 API key 初始化 MPRester
mpr = MPRester(api_key="RVtCSJCsgiKrM059ZGSaZVqPYgBoapvO")

n_sites = 1

docs = mpr.summary.search(num_sites=n_sites)

newRow = ['material_id', 'band_gap', 'formation_energy_per_atom', 'energy_above_hull', 'shear_modulus', 'bulk_modulus', 'is_gap_direct']
csvFile = open("./" + str(n_sites) +"/" + str(n_sites) +".csv", 'a', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
writer.writerow(newRow)  # 数据写入文件中zz
csvFile.close()

epoch = 0
for doc in docs:  # 获取材料索引号
    newRow = []
    epoch += 1
    print('epoch: ', epoch)
    structure = mpr.get_structure_by_material_id(doc.material_id)
    cif_writer = CifWriter(structure)
    cif_writer.write_file("./" + str(n_sites) +"/" + doc.material_id + ".cif")

    newRow = [doc.material_id, doc.band_gap, doc.formation_energy_per_atom, doc.energy_above_hull, doc.shear_modulus, doc.bulk_modulus, doc.is_gap_direct]
    csvFile = open("./" + str(n_sites) +"/" + str(n_sites) +".csv", 'a', newline='', encoding='utf-8')
    writer = csv.writer(csvFile)
    writer.writerow(newRow)  # 数据写入文件中zz
    csvFile.close()

