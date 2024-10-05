# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:09:45 2024

@author: Chang Yen-Yu
"""
#%%
'''
使用.text()函式在座標圖內設定文字
(設定標題是在圖表外,設定文字是在圖表內)
'''
# 匯入套件
import numpy as np
import matplotlib.pyplot as plt

# 設定資料
x = np.array([1,2,3,4,5])
y = x * 2

# 將資料帶入圖表，並設定線條與標記
plt.plot(x, y, 'ro')  #'ro'-> red, 圓形

# 設定文字
plt.text(1,10,'Y=X*2')  # 在(1,10)的位置新增文字'Y=X*2'

# 顯示圖表
plt.show()


#%%
'''
使用legend()函式顯示圖例
圖利: 左上角顯示紅色圓形和框框的部分
'''
# 匯入套件
import numpy as np
import matplotlib.pyplot as plt

# 設定資料
x = np.array([1,2,3,4,5])
y = x * 2

# 將資料帶入圖表，並設定資料與圖例說明
plt.plot(x, y, 'ro', label = 'Y=X*2')

# 設定圖利
plt.legend()

# 顯示圖表
plt.show()


#%%
'''
使用figure()函式建立新圖表及畫布設定
figure(選擇性參數1=value1, 選擇性參數2=value2,...)
'''
# 匯入套件
import numpy as np
import matplotlib.pyplot as plt

# 設定資料
x = np.array([1,2,3,4,5])
y = x * 2

# 設定畫布及相關設定
# figsize為畫布大小，數字只是比例->可以將畫布放大縮小
plt.figure(figsize = (6, 4), facecolor = 'lightblue')
# plt.figure(figsize = (3, 4), facecolor = 'lightgreen')

# 另外一個設定，但spyder圖示看不出來，要存檔開啟才看得出差異
# plt.figure(dpi=300) -> 也是可以將畫布放大縮小

# 將資料帶入圖表，並設定資料與圖例說明
plt.plot(x, y, 'ro')

# 顯示圖表
plt.show()


#%%
'''
使用subplot()函式繪製多張子圖表
subplot(nrows, ncols, plot_number)
subplot有切割定位的功能
'''
# 匯入套件
import numpy as np
import matplotlib.pyplot as plt

# 設定資料
x = np.linspace(-10, 10, 100)  # 從-10到10切成100等分
y1 = 20 * np.sin(x)
y2 = x * x * np.cos(x) + 0.5

# 設定子圖表
plt.subplot(211)  #211-> row切成2部分, column切成1部分, 這圖表放在第1個(上方)
plt.plot(x, y1, 'b-')
plt.subplot(212)  # 212-> row切成2部分, column切成1部分, 這圖表放在第2個(下方)
plt.plot(x, y2, 'r--')

# 顯示圖表
plt.show()


#%%
'''
使用bar()函式繪製長條圖
bar(left, height[選擇性參數1=value1, 選擇性參數2=value2,...])
'''
# 匯入套件
import matplotlib.pyplot as plt
 
# 設定資料
x = [70, 80, 90, 100, 110, 120, 130, 140, 150]
y = [2.2, 3.3, 4.5, 10.7, 12.6, 15.6, 11.2, 5.5, 2.1]
t1 = ['<75', '75-84', '85-94', '95-104', '105-114', '115-124', '125-134', '135-144', '>144']

# 設定畫布大小
plt.figure(figsize = (8,4))

# 設定圖表類型及相關設定
plt.bar(x, y, width=5, tick_label=t1, label='Sample1')  # ticket_label將X軸資料改為t1的資料
plt.legend()
plt.xlabel('Smarts')
plt.ylabel('Probability (%)')
plt.title('Bar of IQ')

# 顯示圖表
plt.show()


#%%
'''
使用hist()函式繪製直方圖
hist(x[, 選擇性參數1=value1, 選擇性參數2=value2,...])
'''
# 匯入套件
import matplotlib.pyplot as plt

# 設定資料
scores = [10, 15, 80, 22, 93, 55, 88, 62, 45, 75, 81, 34, 99, 84, 85, 55, 58, 63, 68, 82, 84]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 設定圖表類型及相關設定
plt.hist(scores, bins, histtype = 'bar')  # scores是資料來源, bins是X的範圍
plt.xlabel('Scores')
plt.ylabel('Students')

# 顯示圖表
plt.show()


#%%
'''
使用pie()函式繪製圓餅圖
pie(x[, 選擇性參數1=value1, 選擇性參數2=value2,...])
'''
# 匯入套件
import matplotlib.pyplot as plt

# 設定資料
activities = ['work', 'sleep', 'rest', 'others']
hours = [12, 6, 3, 3]
colors = ['lightgreen', 'lightblue', 'yellow', 'pink']
explode = [0, 0, 0.1, 0]  # 圓餅圖每個切片和隔壁兩片的距離

# 設定圖表類型及相關設定
plt.pie(hours, labels=activities, colors=colors, shadow=True, explode=explode, autopct='%1.1f%%')  # autopct為格式化設定->圓餅圖上顯示多少%

# 設定正圓
plt.axis('equal')

# 顯示圖表
plt.show()


#%%
# 繪製圓餅圖
# 匯入套件
import matplotlib.pyplot as plt

# 輸入標籤資料
labels = 'Frogs', 'hog', 'Bog', 'Pog'  # 資料型態是tuple

# 輸入圓形圖中各扇形大小，每個扇形的分數面積由x/sum(x)給出
# 扇形是逆時針繪製的，預設情況下從x軸開始
sizes = [20, 30, 40, 10]

# 輸入圓形圖中各扇形顏色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

# 指定用於偏移每個扇形的半徑的分數
explode = (0, 0, 0.1, 0)

# 繪製圓形圖
plt.pie(sizes, explode=explode, labels=labels, colors=colors)

# 設定座標軸尺度相等，所繪出的圓形圖會是正圓
plt.axis('equal')

# 顯示圖形
plt.show()


#%%
# 多圖表應用
# 匯入套件
import matplotlib.pyplot as plt

# 輸入標籤資料
labels = 'Frogs', 'hog', 'Bog', 'Pog'

# 輸入圓形圖中各扇形大小，每個扇形的分數面積由x/sum(x)給出
# 扇形是逆時針繪製的，預設情況下從x軸開始
sizes = [20, 30, 40, 10]

# 輸入圓形圖中各扇形顏色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

# 指定用於偏移每個扇形的半徑的分數
explode = (0, 0, 0.1, 0)

# 指定第一個子圖的位置，繪製長條圖
plt.subplot(1,2,1)  # 分成一列兩欄，在第1欄
plt.bar(labels, sizes, color='red')

# 指定第二個子圖的位置，繪製圓形圖
plt.subplot(1,2,2)  # 分成一列兩欄，在第2欄
plt.pie(sizes, explode=explode, labels=labels, colors=colors)

# 設定座標軸尺度相等，並顯示圖形
plt.axis('equal')  # 正圓形
plt.show()


