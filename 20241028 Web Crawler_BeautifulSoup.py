# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:49:23 2024

@author: Chang Yen-Yu
"""
#%%
'''
使用BeautifulSoup解析Yahoo新聞
'''
import requests
from bs4 import BeautifulSoup

# 設定網址
url = 'https://tw.news.yahoo.com/'

# 擷取此網頁的原始資料，得到一個回應物件res
res = requests.get(url)

# 輸出回應物件的訊息，若是200代表有資料，不是200代表沒有擷取到資料
print(res)

# 輸出回應物件的內容
print(res.text)

# 將網頁資料進行解析
bs = BeautifulSoup(res.text, 'lxml')

# 取出標籤(tag)名稱為li, 屬性(attrib)內容為Pos(r)的資料
data1 = bs.find_all('li', 'Pos(r)')

# 設定編號
x = 1 

# 使用迴圈，將資料逐筆取出並輸出
for i in data1:
    con = i.find('a').text
    print(x, con, sep='.')
    x += 1 


#%%
'''
下載教育部網站的圖片
'''
import requests, os, urlib
from bs4 import BeautifulSoup

# 使用SSL module把證書驗證改成不需要驗證
import ssl
ssl._create_default_https_context = ssl._create_unverified_context()

# 設定教育部網址給變數url
url = 'https://www.edu.tw/'
html = requests.get(url)
html.encoding = 'utf-8'
bs = BeautifulSoup(html.text, 'html.parser')
pics_dir = 'pics'

# 如果工作目錄下沒有pics資料夾，建立一個資料夾
if not os.path.exists(pics_dir):
    os.mkdir(pics_dir)  # 在工作目錄下建立pics資料夾來儲存圖片

# 用串列取得所有<img>標籤的內容
all_links = bs.find_all('img')

# 使用for迴圈對每一個<img>做處理
for link in all_links:
    src = link.get('src')  # 讀取src屬性值的內容
    attrs = [src]  # 將src字串轉成串列attrs
    for attr in attrs:  # 對串列attrs每一項進行處理
        # 如果該項非空(不等於None)，且副檔名為jpg或png        
        if attr != None and ('.jpg' in attr or '.png' in attr):  # 讀取.jpg或.png檔
            full_path = attr  # 設定圖檔完整路徑給變數full_path
            file_n = full_path.split('/')[-1]  # 從網址最右側取得圖檔名稱給變數file_n
            print('==================')
            print('圖檔完整路徑:', full_path)
            try:  # 儲存圖片程式區塊(檔案下載成功)
                image = urllib.request.urlopen(full_path)  # 使用urlopen()取得圖檔資料
                f = open(os.path.join(pics_dir, file_n), 'wb')  # wb:以byte寫入(write)，將下載的圖檔以同檔名寫到資料夾內
                f.write(image.read())
                print('下載成功:%s' %(file_n))
                f.close()
            except:  # 無法儲存圖片程式區塊(檔案下載失敗)
                print('無法下載:%s' %(file_n))
            

