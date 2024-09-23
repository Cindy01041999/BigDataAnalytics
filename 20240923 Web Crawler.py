# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:01:49 2024

@author: Chang Yen-Yu
"""
# urllib套件
# 建立請求
import urllib.request
res = urllib.request.urlopen('https://python.org/')
content = res.read()
print(content)

#%%
# requests套件
# 從網頁擷取原始碼內容
import requests
url = 'https://data.gov.tw/'
html_body = requests.get(url)
html_body.encoding = 'utf-8'
print(html_body.text)

#%%
from bs4 import BeautifulSoup as bs

data = '''
<html><head><title>The Dormouse's story</title></head> <body> <p class="title"><b>The Dormouse's story</b></p> <p class="story">Once upon a time there were three little sisters; and their names were <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.</p> <p class="story">...</p>
''' # 字串str
bsdata = bs(data,'lxml')

print(bsdata)
print(data)

print(bsdata.upper()) 
print(data.upper())

print(bsdata.prettify())
print(data.prettify())  # str不能prettify

print(bsdata.title.text)
#使用find函數找特定標籤
print(bsdata.find('title').text)  # find函數括號內一定要是字串
print(bsdata.find(class_='story').text) # 找標籤為class=story
print(bsdata.find(id='link3').text)  # 找標籤為id=link3
print(bsdata.find(href='http://example.com/lacie').text)

print(bsdata.get_text())

#%%
# find_all()函數
# 找出所有標籤
findalldata = bsdata.find_all('p')
for i in findalldata:
    print(i.text)

# get()函數
# 找出所有超連結a的標籤內的href屬性連結
for link in bsdata.find_all('a'):
    print(link.get('href'))
    
# 找出所有標籤內的class名稱
for className in bsdata.find_all('p'):
    print(className.get('class'))

#%%
from bs4 import BeautifulSoup

html_text = '''
<html><head><title>國立臺灣大學系統</title></head>
<body>
<p class="title"><b>三校聯盟 NTU SYSTEM</b></p>
<p class="ntu_system">
<a href="http://www.ntu.edu.tw" class="union" id="link1">臺灣大學</a>
<a href="http://www.ntnu.edu.tw" class="union" id="link2">臺灣師範大學</a>
<a href="http://www.ntust.edu.tw" class="union" id="link3">臺灣科技大學</a>
</p></body></html>
'''
bs = BeautifulSoup(html_text,'html.parser')

print('1:', bs.title)  # 網頁標題屬性
print('2:', bs.find('a'))  # <a>標籤 -> 使用find函數只會抓取第一個<a>
print('3:', bs.find('b'))  # <b>標籤
print('4:', bs.find_all('a', {'class':'union'}))  # 印出<a>標籤且class為union
print('5:', bs.find('a', {'id':'link2'}))  # 印出<a>標籤且id為link2
print('6:', bs.find('a', {'href':'http://www.ntust.edu.tw'}))  # 印出<a>標籤且href屬性的連結為http://www.ntust.edu.tw

web = bs.find('a', {'id':'link1'})  #取出<a>標籤且id名稱為link1
print('7:', web.get('href'))  # 使用get取出網址

data = bs.select('.union')  #  取出class名稱為union的串列(select會傳回串列)
print('8:', data[0].text)  # 串列的第一項
print('9:', data[1].text)  # 串列的第二項
print('10:', bs.select('#link3'))  # 取出id名稱為link3的串列並印出
