# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:51:03 2024

@author: Chang Yen-Yu
"""
#%%
'''
讀取csv檔案
import csv
with open(檔案名稱, encoding='utf8') as xxx:
    csvReader = csv.reader(xxx)
'''
# 建立Reader物件，再轉成串列後輸出
import csv

fn = 'csvReport.csv'
# 開啟csv檔案
with open(fn, encoding='utf8') as csvFile:
    csvReader = csv.reader(csvFile)  # 讀取檔案物件建立Reader物件
    listReport = list(csvReader)  # 將資料轉為串列

print(listReport)


#%%
# 使用索引列出特定串列內容
import csv

fn = 'csvReport.csv'
with open(fn, encoding='utf8') as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)  # 讀取檔案建立Reader物件
    listReport = list(csvReader)
    
print(listReport[0][1], listReport[0][2])
print(listReport[1][1], listReport[1][2])
print(listReport[3][1], listReport[3][2])


#%%
'''
寫入csv檔案
with open('檔案名稱', 'w', newline='', encoding='utf8') as csvFile:
    outWriter = csv.writer(csvFile)
    
newline='' -> 可避免輸出時多空一行
'''
# withrow()函式寫入串列資料
import csv

fn = 'csvoutput.csv'
with open(fn, 'w', newline='', encoding='utf-8') as csvFile:  # 開啟csv檔
    csvWriter = csv.writer(csvFile)  # 建立Writer物件
    csvWriter.writerow(['姓名', '電話', 'ID'])
    csvWriter.writerow(['李小明', '(02)22345678', 'A120888320'])
    csvWriter.writerow(['王大強', '(03)8565678', 'Z999888765'])


#%%
'''
可用delimiter分隔符號更改各欄間的逗號設定
當用'\t'字元取代逗號, 用Excel開啟會將每航行資料放在一起
'''
import csv

fn = 'csvoutput2.csv'
with open(fn, 'w', newline='', encoding='utf-8') as csvFile:  # 開啟csv檔
    csvWriter = csv.writer(csvFile, delimiter='\t')
    csvWriter.writerow(['姓名', '電話', 'ID'])
    csvWriter.writerow(['李小明', '(02)22345678', 'A120888320'])
    csvWriter.writerow(['王大強', '(03)8565678', 'Z999888765'])


#%%
# 先讀csv檔, 再將檔案寫入另一個檔案，達成copy目的
import csv

infn = 'csvReport.csv'  # 來源檔案
outfn = 'csvoutput.csv'  # 目的檔案

with open(infn, encoding='utf8') as csvRFile:  # 開啟csv檔供讀取
    csvReader = csv.reader(csvRFile)  # 讀取檔案建立Reader物件
    listReport = list(csvReader)  # 將資料轉成串列
    
with open(outfn, 'w', newline='', encoding='utf8') as csvOFile:  # 開啟csv檔供寫入
    csvWriter = csv.writer(csvOFile)  # 建立Writer物件
    for row in listReport:
        csvWriter.writerow(row)  # 將串列寫入
        
