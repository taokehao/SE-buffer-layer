# import pandas as pd
#
# # 加载数据
# predict_df = pd.read_csv('/path/to/predict-21686.csv', header=None, names=['id', 'prediction'])
# true_df = pd.read_csv('/path/to/true-889.csv', header=None, names=['id', 'label'])
#
# # 将 true_df 转换为字典，便于快速查找标签
# true_dict = dict(zip(true_df.id, true_df.label))
#
# # 定义一个函数，用于根据预测数值或已知标签来标记数据
# def label_prediction(row):
#     # 使用预测数值判断标签（大于0.5为1，否则为0）
#     return 1 if row['prediction'] > 0.5 else 0
#
# # 应用函数，创建新的标签列
# predict_df['label'] = predict_df.apply(label_prediction, axis=1)
#
# # 移除在 true_df 中出现的 ID
# filtered_df = predict_df[~predict_df['id'].isin(true_df['id'])]
#
# # 再移除所有标签为 0 的行
# final_df = filtered_df[filtered_df['label'] == 1]
#
# # 保存处理后的数据到 CSV 文件
# output_file_path = '/path/to/filtered_labeled_predictions.csv'
# final_df.to_csv(output_file_path, index=False)


import pandas as pd

# 加载数据
predict_df = pd.read_csv('./predict-21686.csv', header=None, names=['id', 'prediction'])
true_df = pd.read_csv('./true-889.csv', header=None, names=['id', 'label'])

# 将 true_df 转换为字典，便于快速查找标签
true_dict = dict(zip(true_df.id, true_df.label))

# 定义一个函数，用于根据预测数值或已知标签来标记数据
def label_prediction(row):
    # 使用预测数值判断标签（大于0.5为1，否则为0）
    return 1 if row['prediction'] > 0.5 else 0

# 应用函数，创建新的标签列
predict_df['label'] = predict_df.apply(label_prediction, axis=1)

# 移除在 true_df 中出现的 ID
filtered_df = predict_df[~predict_df['id'].isin(true_df['id'])]

# 再移除所有标签为 0 的行
final_df = filtered_df[filtered_df['label'] == 1]

# 保存处理后的数据到 CSV 文件
output_file_path = './filtered_labeled_predictions.csv'
final_df.to_csv(output_file_path, index=False)
