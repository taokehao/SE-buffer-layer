import pandas as pd

# 定义不适用的元素列表
unsuitable_elements = ["Pb", "Cd", "Hg", "Be", "U", "Th", "As", "Se", "Tl", "Sb", "Ge", "La", "Ce", "Pr", "Nd", "Pm",
                       "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Zr", "W", "Hf", "Np", "Am", "Cm",
                       "Es", "No", "Lr", "Ac", "Md"]

# 加载数据
df = pd.read_csv('./filtered_labeled_predictions_updated.csv')

# 筛选出不包含不适用元素的行
# 先将'包含元素'列的字符串转换为列表，然后检查列表中的元素是否在unsuitable_elements中
filtered_df = df[~df['包含元素'].apply(lambda x: any(elem in unsuitable_elements for elem in x.split(', ')))]

# 保存更新后的DataFrame到CSV文件
filtered_df.to_csv('./filtered_labeled_predictions_final.csv', index=False)
