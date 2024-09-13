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
predict_df = pd.read_csv('./filtered_labeled_predictions.csv')
formula_list = []
elements_list = []
for i in predict_df['id']:
    mp_id = 'mp-' + str(i)
    print(mp_id)
    structure = mpr.summary.search(material_ids=mp_id, fields=["elements", "formula_pretty"])[0]
    formula = structure.formula_pretty
    formula_list.append(formula)
    element = structure.elements
    element_list = []
    for i in element:
        element_list.append(i.name)
    elements_list.append(element_list)
# 将元素列表转换为没有中括号的字符串
elements_list = [', '.join(element) for element in elements_list]

# 在DataFrame中添加两个新的列
predict_df['化学式'] = formula_list
predict_df['包含元素'] = elements_list

# 保存更新后的DataFrame到CSV文件
predict_df.to_csv('./filtered_labeled_predictions_updated.csv', index=False)
