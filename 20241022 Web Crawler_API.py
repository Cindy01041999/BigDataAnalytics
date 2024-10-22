# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:28:52 2024

@author: Chang Yen-Yu
"""
#%%
'''
API應用-新北市圖書館名冊(CSV)
'''
import requests as rq  # 載入requests套件，縮寫rq
import csv  # 載入csv套件，以處理csv格式
import pandas as pd  # 載入pandas套件

# 開放資料:新北市圖書館
url = 'https://data.ntpc.gov.tw/api/datasets/4a03827a-588b-4058-ab21-ec02283e2bb7/csv?size=100'

# 對url發出get請求
r = rq.request('GET', url)

# 轉換成串列 方式一
data = list(csv.reader(r.text.split()))

# 轉換成串列 方式二
# x = r.text.split()
# y = csv.reader(x)
# data2 = list(y)

# 將資料集串列轉換成DataFrame
df = pd.DataFrame(data[1:], columns=['縣市', '區域', '圖書館名稱', '地址'])

# 資料順序改從1開始
df.index += 1 
print(df)


#%%
'''
API應用-新北市政府行政園區會場資訊及收費標準(JSON)
'''
# 載入requests套件
import requests as rq

# 開放資料: 新北市政府行政園區會場資訊及收費標準
url = 'https://data.ntpc.gov.tw/api/datasets/e3fffcab-4de7-4dcf-919b-337cc9b45a48/json?size=100'

# 提出get請求，並將回傳內容轉成json格式(JSON陣列轉Python串列list)
html_content = rq.get(url)
json_data = html_content.json()

# item_detail是list中的元素，型態為字典(dict)
for item_detail in json_data[:9]:
    print_info = '地址:' + item_detail['address'] + ',' + '容量:' + item_detail['capacity'] + ',' + '費用:' + item_detail['caution_money']
    print(print_info)

