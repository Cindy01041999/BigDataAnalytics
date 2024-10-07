# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:51:40 2024

@author: Chang Yen-Yu
"""
#%%
'''
多元線性迴歸 Multiple Regression Analysis
使用身高和腰圍來預測體重
'''
# 1.匯入套件
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

-----
# 2.設定來源資料 
# 建立Numpy陣列
waist_heights = np.array([[67,160], [68,165], [70,167], [65,170], [80,165],
                         [85,167], [78,178], [79,182], [95,175], [89,172]])
weights = np.array([50, 60, 65, 65, 70 ,75, 80, 85, 90, 81])

# 轉至成DataFrame物件
x = pd.DataFrame(waist_heights, columns=['Waist', 'Height'])
y = pd.DataFrame(weights, columns=['Weight'])

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
# 4.進行預測，使用predict()函數預測腰圍和身高[66,164], [82,172]的體重
new_waist_heights = pd.DataFrame(np.array([[66,164], [82,172]]))
predicted_weights = lm.predict(new_waist_heights)
print(predicted_weights)


