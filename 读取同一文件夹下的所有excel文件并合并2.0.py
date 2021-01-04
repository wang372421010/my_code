import pandas as pd
import os

# 读取excl

dir = os.path.realpath("./")
suffix = ".xlsx"
concat_data = pd.read_excel(dir + "\\2020年01-06月.xlsx")  # 以某一个表作为主表
res = []
for root, directory, files in os.walk(dir):
    for filename in files:
        name, suf = os.path.splitext(filename)
        if suf == suffix:
            res.append(os.path.join(root, filename))
for file_name in res:
    try:
        for sheet in range(0, 30):
            info = pd.read_excel(file_name, sheet_name=sheet, index=False)
            concat_data = concat_data.append(info)
    except:
        continue

concat_data = concat_data.drop_duplicates(["审批编号"], keep="last")

"""
dir = os.path.realpath('./')
suffix = '.csv'
# 读取csv
concat_data = pd.read_csv(dir + '\\5月工单-udesk.csv',encoding='gbk')
res = []
for root, directory, files in os.walk(dir): 
    for filename in files:
        name, suf = os.path.splitext(filename)
        if suf == suffix:
            res.append(os.path.join(root, filename))
for file_name in res:
    info = pd.read_csv(file_name,encoding='gbk')
    concat_data = concat_data.append(info)
concat_data = concat_data.drop_duplicates(['编号'], keep="last")
"""


concat_data.to_excel(dir + "\\concat_data.xlsx", index=False)  # 输出表名

