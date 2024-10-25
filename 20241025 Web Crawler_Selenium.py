# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:20:50 2024

@author: Chang Yen-Yu
"""
'''
使用Selenium開啟Chrome網頁
'''
from selenium import webdriver
import time

# 使用selenium開啟Chrome瀏覽器
driver = webdriver.Chrome()
driver.implicitly_wait(5)  # 網路載入需要時間(設定5秒)
driver.get('https://tw.news.yahoo.com/')
print(driver.page_source)

# 等待3秒
time.sleep(3)  # 瀏覽器開啟3秒後再關閉

# 關閉Chrome瀏覽器
driver.quit()


#%%
'''
使用Selenium連續開啟多個網頁, 搭配迴圈及等待機制達成
'''
# 3個網站的網址
urls = ['https://24h.pchome.com.tw',
        'https://shopee.tw',
        'https://www.momoshop.com.tw']

# 開啟Chrome瀏覽器
driver = webdriver.Chrome()

# 用迴圈依序開啟3個網站
for url in urls:
    driver.get(url)
    time.sleep(5)
    
# 關閉Chrome瀏覽器
driver.quit()


#%%
'''
下載網頁:Selenium取得的是瀏覽器即時產生的HTML程式碼，可以搭配
BeautifulSoup解析後取得原始程式碼
'''
from selenium import webdriver
from bs4 import BeautifulSoup

# 使用Selenium開啟Chrome瀏覽器
driver = webdriver.Chrome()
driver.get('https://tw.yahoo.com/')

# 用BeautifulSoup解析欲爬取的頁面原始碼
data = BeautifulSoup(driver.page_source, 'lxml')

# 將解析後的原始碼寫成檔案
# write()要使用prettify來放置格式化的程式碼
with open('getyahoo.html', 'w', encoding='utf-8') as file:
    file.write(data.prettify())
    
driver.quit()

