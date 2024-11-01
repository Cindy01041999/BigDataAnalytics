# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:55:26 2024

@author: Chang Yen-Yu
"""
#%%
'''
台灣彩券-by期別
'''
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 用以儲存所爬到的大樂透號碼
lotto_list = []

driver = webdriver.Chrome()
driver.get('https://www.taiwanlottery.com/lotto/result/lotto649')

# 輸入期別進行查詢
while True:
    try:
        number = input('請輸入期別:')
        if number.isdigit() == True:
            element = driver.find_element(By.ID, 'el-id-1024-2')
            element.clear()
            element.send_keys(number)
            driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[2]/div/nav/div[4]/button').click()
            time.sleep(3)
            data = driver.find_elements(By.CLASS_NAME, 'special-number')
            print('開獎號碼', end = ' : ')
            for i in data[:-1]:  # 取到倒數第2個數字(不含-1)
                print(i.text, end=' ')
            print('特別號:', data[-1].text)
        else:
            print('出現問題，重新輸入!')
            continue
    except:
        print('出現問題，重新輸入!')
        continue
    check = input('請問還要繼續嗎? 繼續請輸入Y, 其他輸入均會離開:')
    if check.upper() != 'Y':
        print('已結束，謝謝!')
        break
driver.quit()


#%%
'''
台灣彩券-by年份
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.taiwanlottery.com/lotto/result/lotto649')
time.sleep(3)

try:
    mon_form = '//*[@id="el-id-1024-3"]/div/div[1]/div/div[2]/table/tbody/tr[{}]/td[{}]/div/span'
    for i in range(1, 4):  # 第1-3列
        for j in range(1, 5):  # 第1-4行
            driver.find_element(By.XPATH,'''//*[@id="__nuxt"]/main/div/[1]/div[2]/div/nav/div[4]/form/div[2]/div/div/div''').click()
            time.sleep(1)
            mon = mon_form.format(i, j)
            if 'span' not in mon:
                break
            print(mon)  # 確認格式
            time.sleep(1)
            driver.find_element(By.XPATH, mon).click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[2]/div/nav/div[4]/button').click()
            time.sleep(1)
            periodtitle = driver.find_elements(By.CLASS_NAME, 'period-title')
            periodtitle = [i.text for i in periodtitle]
            periodtitle = periodtitle[::-1]  # 期數順序調整 9~1期 -> 1~9期
            data = driver.find_elements(By.CLASS_NAME, 'special-number')
            data = [i.text for i in data]
            data = data[::-1]  # 樂透號碼順序調整
            print(len(periodtitle))  # 確認數量
            print(len(data))  # 確認數量
            
            # 方法(1):樂透號碼為由大到小
            for p in periodtitle:
                print(p)
                print('開出號碼:', end='')
                for _ in range(6):  # 選取index=1~最後一數字(因為index=0的數字為特別號，不用選取)
                    print(data.pop(1), end=' ')
                print('特別號:', data.pop(0), sep='')
                print()
            
            # 方法(2):樂透號碼為小到大(有特別做反轉reverse)
            for p in periodtitle:
                print(p)
                print('開出號碼:', end='')
                number = []
                for _ in range(6):
                    number.append(data.pop(1))
                number.reverse()  # 樂透號碼數字從由大到小->改為由小到大
                for n in number:
                    print(n, end='')
                print('特別號:', data.pop(0), sep='')
                print()
except:
    print('出現問題，程式結束!')

print('順利完成，程式結束!')
driver.close()
            
                