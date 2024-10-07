# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:52:01 2024

@author: Chang Yen-Yu
"""
#%%
'''
簡單線性回歸 Simple Linear Regression
用氣溫預測業績
'''
# 1.匯入套件
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

-----
# 2.設定來源資料 
# 建立Numpy陣列
temperatures = np.array([29, 28, 34, 31, 25, 29, 32, 31, 24, 33, 25, 31, 26, 30])
drink_sales = np.array([7.7, 6.2, 9.3, 8.4, 5.9, 6.4, 8.0, 7.5, 5.8, 9.1, 5.1, 7.3, 6.5, 8.4])

# 轉至成DataFrame物件
x = pd.DataFrame(temperatures, columns = ['Temperature'])
y = pd.DataFrame(drink_sales, columns = ['Drrnk_Sales'])

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
# 4.進行預測，使用predict()函數預測氣溫26, 30度的業績
new_temperatures = pd.DataFrame(np.array([26, 30]), columns=['Temperature'])
predicted_sales = lm.predict(new_temperatures)
print(predicted_sales)

-----
# 5.使用Matplotlib繪製散佈圖
plt.scatter(temperatures, drink_sales)  # 繪圖
regression_sales = lm.predict(x)  # 使用x變數計算預測的y值
plt.plot(temperatures, regression_sales, color='blue')  # 繪出藍線
plt.plot(new_temperatures, predicted_sales, color='red', marker='o', markersize=10)  # 繪出2個預測的新溫度(2個紅點)
plt.show()


