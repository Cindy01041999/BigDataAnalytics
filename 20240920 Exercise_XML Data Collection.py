# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:13:09 2024

@author: Chang Yen-Yu
"""
import xml.etree.ElementTree as et
import csv
fn = 'write.csv'

tree = et.ElementTree(file='bicycle.xml')
root = tree.getroot()

for row in root.findall('row'):
    print(row.find('sna').text, row.find('sarea').text, row.find('ar').text)


with open(fn, 'w', newline='', encoding='utf-8') as csvFile:
    csvWriter = csv.writer(csvFile)
    for row in root.findall('row'):
        csvWriter.writerow([row.find('sno').text, row.find('sna').text, row.find('tot').text])
        


    
