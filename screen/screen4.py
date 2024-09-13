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
predict_df = pd.read_csv('./filtered_labeled_predictions_final.csv')

# 创建一个列表来存储满足条件的行
selected_rows = []

for i in predict_df['id']:
    mp_id = 'mp-' + str(i)
    mp_id = 'mp-557268'
    print(mp_id)
    # 使用搜索条件检索特定字段
    try:
        structure = mpr.summary.search(material_ids=mp_id, fields=['energy_above_hull', 'band_gap'])[0]
        energy_above_hull = structure.energy_above_hull
        band_gap = structure.band_gap
        # 检查是否符合条件
        if band_gap > 3 and energy_above_hull == 0:
            # 如果满足条件，则添加到selected_rows列表
            selected_rows.append(predict_df[predict_df['id'] == i])
    except IndexError:
        # 如果没有找到数据，跳过当前id
        print(f"No data found for {mp_id}")

# 使用 pd.concat() 合并所有选中的行
if selected_rows:
    selected_df = pd.concat(selected_rows)
    # 保存选中的数据到新的CSV文件
    selected_df.to_csv('./selected_materials.csv', index=False)
else:
    print("No materials found that match the criteria.")
