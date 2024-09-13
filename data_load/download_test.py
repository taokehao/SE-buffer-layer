from mp_api.client import MPRester

# mpr = MPRester(api_key="RVtCSJCsgiKrM059ZGSaZVqPYgBoapvO")
#
#
# # electronic_doc = mpr.electronic_structure.search(material_ids=["mp-975333"])
# electronic_doc = mpr.materials.electronic_structure.search(material_ids=["mp-773089"])
# # elasticity_doc = mpr.elasticity.search("mp-763425")
# lll = electronic_doc[0].band_gap
# print(lll)


from mp_api.client import MPRester
import warnings
warnings.filterwarnings("ignore")

mpr = MPRester(api_key="RVtCSJCsgiKrM059ZGSaZVqPYgBoapvO")
docs = mpr.summary.search(elements=["Li", "Fe", "P", "O"],
                          fields=["material_id"])

id_list_all = []
id_list_vrh = []
vrh_list = []
epoch = 1
for doc in docs:  # 获取材料索引号
    print('epoch: ', epoch)
    id_list_all.append(doc.material_id)
    print(doc.material_id)
    elasticity_doc = mpr.elasticity.search(doc.material_id)
    if len(elasticity_doc) != 0:
        if elasticity_doc[0].shear_modulus is not None:
            id_list_vrh.append(doc.material_id)
            vrh = elasticity_doc[0].shear_modulus.vrh
            vrh_list.append(vrh)
            print('此时第', len(vrh_list), '个vrh: ', vrh)
    epoch += 1

file = open('id_list_all.txt', 'w')
for i in id_list_all:
    print(i, file=file)
file.close()

file = open('id_list_vrh.txt', 'w')
for i in id_list_vrh:
    print(i, file=file)
file.close()

file = open('vrh_list.txt', 'w')
for i in vrh_list:
    print(i, file=file)
file.close()
