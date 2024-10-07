# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:13:09 2024

@author: Chang Yen-Yu
"""
'''
請撰寫程式,讀取新北市公共自行車即時資訊 bicycle.xml,並進行以下處理。
    1.請將其中 sna、sarea、ar 等三個欄位內容輸出。
    2.請將其中 sno、sna、tot 等三個欄位轉存為 write.csv。
'''

import xml.etree.ElementTree as et
import csv
fn = 'write.csv'

tree = et.ElementTree(file='bicycle.xml')
root = tree.getroot()

# sna、sarea、ar 等三個欄位內容輸出
for row in root.findall('row'):
    print(row.find('sna').text, row.find('sarea').text, row.find('ar').text)

# sno、sna、tot 等三個欄位轉存為 write.csv
with open(fn, 'w', newline='', encoding='utf-8') as csvFile:
    csvWriter = csv.writer(csvFile)
    for row in root.findall('row'):
        csvWriter.writerow([row.find('sno').text, row.find('sna').text, row.find('tot').text])
        


    
