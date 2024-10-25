# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:08:02 2024

@author: Chang Yen-Yu
"""
#%%
'''
正則表示式 Regular Expression
'''
# 查詢字串中的數字:
import re
pattern = re.compile(r'\d+')  # 查詢數字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)  # index=0-9之間的數字
print(result1)
print(result2)


#%%
import re
key = 'abcde@abc.edu.tw'
p1 = '@.+.'  # @後面至少2字以上
pattern1 = re.compile(p1)
print(pattern1.findall(key))

p1 = '@.+\.'  # 開頭@,結尾是.,中間至少1字以上
pattern1 = re.compile(p1)
print(pattern1.findall(key))

p1 = '@.+?\.'  # 開頭@,結尾是.,中間為勉強模式(長度最短的符合文字)
pattern1 = re.compile(p1)
print(pattern1.findall(key))


#%%
import requests
import re  # 正則表示式(Regular Expression Operations)

url = input('請輸入網址(需包含http://):')
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    pattern = input('請輸入欲搜尋的字串:')  # pattern存放欲搜尋的字串
    # 判斷是否曾有搜尋到
    if pattern in htmlfile.text:
        print('搜尋 %s 成功' % pattern)
    else:
        print('搜尋 %s 失敗' % pattern)
    # 計算出現次數
    name = re.findall(pattern, htmlfile.text)
    if name != None:
        print('%s 出現 %d 次' % (pattern, len(name)))
    else:
        print('%s 出現 0 次' % pattern)
else:
    print('網頁下載失敗')


#%%
import requests
import re
from bs4 import BeautifulSoup

resp = requests.get('https://bit.ly/3gkZaJa')
soup = BeautifulSoup(resp.text, 'lxml')

# 找出所有'h'開頭的標題文字
titles = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
for title in titles:
    print(title.text.strip())

# 利用regex找出所有'h'開頭的標題文字
for title in soup.find_all(re.compile('h[1-6]')):
    print(title.text.strip())

# 找出所有.png結尾的圖片
imgs = soup.find_all('img')
for img in imgs:
    if 'src' in img.attrs:
        if img['src'].endswith('.png'):
            print(img['src'])
            
# 利用regex找出所有.png結尾的圖片
for img in soup.find_all('img', {'src':re.compile('\.png$')}):  # '\.png$' -> .png結尾的字串
    print(img['src'])
    
#  找出所有.png結尾且含'beginner'的圖片
imgs = soup.find_all('img')
for img in imgs:
    if 'src' in img.attrs:
        if 'begineer' in img['src'] and img['src'].endswith('.png'):
            print(img['src'])
            
# 利用regrex找出所有.png結尾且含'begineer'的圖片
# 'begineer.*\.png$' -> 檔名為.png且含有begineer的字串,begineer字串與檔名之間可以間隔0或多個字元
for img in soup.find_all('img', {'src': re.compile('begineer.*\.png$')}):
    print(img['src'])

