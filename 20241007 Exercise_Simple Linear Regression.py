# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:26:33 2024

@author: Chang Yen-Yu
"""
#%%
'''
請建立簡單線性迴歸預測模型，預測學生的身高、體重
Questions:
    1.預測身高155,165,180的體重。體重請輸出至小數點1位，另外也輸出其迴歸係數與截距。
    2.預測體重55,65,70的身高並以圖表示，身高請輸出至整數。
'''

# 1.匯入套件
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

-----
# 2.設定來源資料 
# 建立Numpy陣列
height = np.array([147, 163, 159, 155, 163, 158, 172, 161, 153, 161])
weight = np.array([51, 60, 57, 53, 60, 55, 68, 59, 56, 62])

# 轉至成DataFrame物件
x = pd.DataFrame(height, columns = ['Height'])
y = pd.DataFrame(weight, columns = ['Weight'])

-----
# 3.建立模型
'''
程式碼建立 LinearRegression 物件後，呼叫fit()函數訓練模型
fit(解釋變數, 反應變數)
'''
lm = LinearRegression()
lm.fit(x, y)

'''
模型訓練完後，使用coef_屬性得到迴歸係數、intercept_屬性得到截距
'''
print('迴歸係數:', lm.coef_)
print('截距:', lm.intercept_)

-----
# 4.進行預測，使用predict()函數預測
# a.預測身高155,165,180的體重
new_height = pd.DataFrame(np.array([155, 165, 180]), columns=['Height'])
predicted_weight = lm.predict(new_height)
print('身高155,體重預測%.1f' % predicted_weight[0][0])
print('身高165,體重預測%.1f' % predicted_weight[1][0])
print('身高180,體重預測%.1f' % predicted_weight[2][0])

# b.預測體重55,65,70的身高並以圖表示
lm.fit(y, x)
new_weight = pd.DataFrame(np.array([55, 65, 70]), columns=['Weight'])
predicted_height = lm.predict(new_weight)
print('體重55,身高預測%d' % predicted_height[0][0])
print('體重65,身高預測%d' % predicted_height[1][0])
print('體重70,身高預測%d' % predicted_height[2][0])

-----
# 5.使用Matplotlib繪製散佈圖
plt.scatter(weight, height)  # 繪圖
regression_height = lm.predict(y)  # 使用y變數計算預測的x值
plt.plot(weight, regression_height, color='blue')  # 繪出藍線
plt.plot(new_weight, predicted_height, color='red', marker='o', markersize=10)  # 繪出3個預測的新身高(3個紅點)
plt.show()

