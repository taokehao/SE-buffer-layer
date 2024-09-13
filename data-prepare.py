import os
from mp_api.client import MPRester
import warnings
from pymatgen.io.cif import CifWriter
warnings.filterwarnings("ignore")

# 使用 API key 初始化 MPRester
mpr = MPRester(api_key="RVtCSJCsgiKrM059ZGSaZVqPYgBoapvO")

id_list_all = open("./data_load/id_list_vrh.txt", 'r').readlines()
epoch = 0
for mp in id_list_all:
    name = mp.strip('\n')
    epoch += 1
    print('epoch: ', epoch)
    structure = mpr.get_structure_by_material_id(name)
    cif_writer = CifWriter(structure)
    cif_writer.write_file("./data/sample-classification/" + name + ".cif")


# # 使用 API key 初始化 MPRester
# mpr = MPRester(api_key="RVtCSJCsgiKrM059ZGSaZVqPYgBoapvO")
#
# id_list_all = open("./data_load/id_list_all.txt", 'r').readlines()
# epoch = 0
# band_gap = []
# for mp in id_list_all:
#     name = mp.strip('\n')
#     epoch += 1
#     print('epoch: ', epoch)
#     structure = mpr.summary.search(material_ids=name)[0]
#     band_gap.append(structure.band_gap)
#
#
# file = open('./data_load/label_list.txt', 'w')
# for i in band_gap:
#     print(i, file=file)
# file.close()


# # 假设这是包含上述文件的文件夹路径
# folder_path = './data/sample-classification'
#
# # 列出给定文件夹内的所有文件
# files = os.listdir(folder_path)
#
# # 遍历文件夹内的每个文件
# for filename in files:
#     if filename.startswith('mp-'):
#         # 生成新的文件名（去掉 'mp-' 前缀）
#         new_filename = filename.split('mp-')[-1]
#         # 生成当前文件的完整路径
#         original_file = os.path.join(folder_path, filename)
#         # 生成新文件的完整路径
#         new_file = os.path.join(folder_path, new_filename)
#         # 重命名文件
#         os.rename(original_file, new_file)
