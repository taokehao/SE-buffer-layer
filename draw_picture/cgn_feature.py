# import numpy as np
# import csv
# nbr_fea = np.load("./input/nbr_fea.npy").tolist()
# nbr_fea_idx = np.load("./input/nbr_fea_idx.npy").tolist()
#
# count1 = 0
# for idx in nbr_fea_idx:
#     newRow = []
#     for i in range(100):
#         newRow.append(0)
#     count2 = 0
#     for id in idx:
#         newRow[id] = nbr_fea[count1][count2]
#         count2 += 1
#     count1 += 1
#     csvFile = open("./output/图2-3.csv", 'a', newline='', encoding='utf-8')
#     writer = csv.writer(csvFile)
#     writer.writerow(newRow)  # 数据写入文件中zz
#     csvFile.close()


import numpy as np
import csv
nbr_fea = np.load("./input/nbr_fea_2.npy")
nbr_fea_idx = np.load("./input/nbr_fea_idx_2.npy")

count1 = 0
for idx in nbr_fea_idx:
    count2 = 0
    for id in idx:
        newRow = []
        newRow = nbr_fea[count1][count2].tolist()
        count2 += 1
        csvFile = open("./output/图2-3.csv", 'a', newline='', encoding='utf-8')
        writer = csv.writer(csvFile)
        writer.writerow(newRow)  # 数据写入文件中zz
        csvFile.close()
    count1 += 1
    break
