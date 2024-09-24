# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:44:12 2024

@author: Chang Yen-Yu
"""
#%%
# 使用plot()繪圖函式繪製線條
# 匯入套件
import numpy as np
import matplotlib.pyplot as plt  #Python視覺化套件

# 設定資料
x = np.arange(0, 5, 0.1)  #從0到5,間隔0.1
y = np.square(x)  #y=x的平方

# 將資料帶入圖表
plt.plot(x, y)  #將x,y資料帶入成為折線圖
"""
線條色彩&標記:
'r--' -> red, 虛線'--'
'bs' -> blue, 方形標記's'
'g^' -> green, 三角標記(向上)'^'
x**2 -> y=x的2次方
"""
plt.plot(x, x, 'r--', x, x**2, 'bs', x, x**3, 'g^')  # 產出折線圖並設定線條及標記

# 顯示圖表
plt.show()  #顯示折線圖在右方"Plots"欄位

#%%
# 使用title(s)函式設定圖表標題
# 匯入套件
import numpy as np
import matplotlib.pyplot as plt

# 設定資料
x = np.array([1,2,3,4,5])
y = x * 2

# 將資料帶入圖表, 並進行相關設定
plt.plot(x, y, 'ro')  #ro -> red, 圓形'o'

# 設定標題及位置
plt.title('Y=X*2', loc='right')  #標題位置在右邊

# 顯示圖表
plt.show()

#%%
# 使用xlabel()和ylabel()函式設定座標軸名稱
# 匯入套件
import matplotlib.pyplot as plt

# 設定資料
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
pops = [2.5, 2.7, 3.3, 4, 4.8, 6.1, 7]

# 將資料帶入圖表, 並進行相關設定
plt.plot(years, pops)
plt.title('Population Growth')  #設定標題

# 設定X、Y軸名稱
plt.xlabel('Population growth by year')
plt.ylabel('Population in billions')

# 顯示圖表
plt.show()

#%%
# 中文字體顯示設定->在繪圖中使用中文
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

#1 中文的基本設定(影響全部程式)
plt.rcParams['font.family'] = 'Microsoft YaHei'  #設定字體 #Param=Parameter
plt.rcParams['font.size'] = 12  #設定字體大小

#2 只適用於指定地方的中文設定
# font_path指定字型的完整路徑
font_path = 'C:\Windows\Fonts\mingliu.ttc' #從電腦本地端抓取字體
font_prop = fm.FontProperties(fname = font_path)
font_prop.set_style('normal')  #字型(標準/粗體/斜體)
font_prop.set_size('12')  #字體大小

# 以上僅為設定, 接下來要帶入X、Y
plt.plot([-1,2,3], [2,-12,8])  #產出折線圖=>點(-1,2)(2,-12)(3,8)
plt.xlabel('X軸標籤', size=26)  #設定X軸名稱、X軸字體大小
plt.ylabel('Y軸標籤', fontproperties=font_prop, rotation=0, fontsize=16, ha='right')  #設定Y軸名稱&其他設定
"""
Y軸有特別設定字型(帶入font_prop),X軸沒有,所以X、Y軸字型不同
rotation=0 -> Y軸的字是水平的
字體大小為16(前面有設定過size=12, 但以最後設定的為主)
ha='right -> 水平對齊線, 代表Y軸名稱的最後一個字靠右對齊Y軸數字(不會疊到數字)
""" 
plt.show()

#%%
# 使用xlim(),ylim()或axis()函式設定座標軸範圍
# 使用grid()設定格線

# 匯入套件
import numpy as np
import matplotlib.pyplot as plt

# 設定資料
x = np.array([1,2,3,4,5])
y = x * 2

# 將資料帶入圖表, 並進行相關設定
plt.plot(x, y, 'ro')  #ro: red, 圓形'o'

# 設定座標軸範圍
plt.xlim(-10, 10)
plt.ylim(-50, 50)
# 方法2: plt.axis([-10, 10, -50, 50])

# 設定格線
plt.grid()

# 顯示圖表
plt.show()

#%%
# 使用xticks(),yticks()設定座標軸標籤
# 使用minorticks_on()設定座標軸次刻度線

# 匯入套件
import numpy as np
import matplotlib.pyplot as plt

# 設定座標軸名稱
plt.xlabel('Age')
plt.ylabel('Monthly Salary')

# 設定座標軸標籤
plt.xticks(np.arange(5),("", "<=30", "31~60", "61~100", ""))  # 座標軸上每個標籤的數值
plt.yticks(np.arange(5),("", "<25K", "25K~50K", "51K~80K", ">80K"))

# 設定顯示次刻度線->座標軸標籤與標籤之間的刻度
plt.minorticks_on()

# 圖表輸出
plt.show()
