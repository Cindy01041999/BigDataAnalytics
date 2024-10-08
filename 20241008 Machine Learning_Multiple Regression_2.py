# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:22:12 2024

@author: Chang Yen-Yu
"""
#%%
from sklearn.linear_model import LinearRegression
'''
多元線性迴歸:使用加州房價資料集預測房價
1. 載入資料集
2. 建立DataFrame物件
'''
# 載入資料集
from sklearn import datasets
california = datasets.fetch_california_housing()
print(california.keys())
print(california.data.shape)  # data是房屋特徵資料(8個欄位20640筆資料)
print(california.feature_names)  # feature_names是房屋特徵名稱
print(california.target_names)  # target_names是房價名稱
print(california.DESCR)  # DESCR是資料集描述

# 使用data屬性建立DataFrame物件
import pandas as pd
from sklearn import datasets

california = datasets.fetch_california_housing()
x = pd.DataFrame(california.data, columns=california.feature_names)  # 設定欄位名稱為feature_names
print(x.head())  # 顯示前5筆資料

# 建立應變數y的DataFrame物件target
target = pd.DataFrame(california.target, columns=california.target_names)
# target = pd.DataFrame(california.target, columns=['MEDV'])  # 欄位名稱自訂為MEDV
print(target.head())  # 顯示前5筆資料


#%%
'''
多元線性迴歸:使用加州房價資料集預測房價
3. 呼叫fit()函數訓練預測模型
'''
# 載入套件&資料集
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 設定資料
california = datasets.fetch_california_housing()

# 建立DataFrame物件
x = pd.DataFrame(california.data, columns=california.feature_names)
y = pd.DataFrame(california.target, columns=['MEDV'])

# 呼叫fit()函數訓練預測模型
lm = LinearRegression()
lm.fit(x, y)

print('迴歸係數:', lm.coef_)
print('截距:', lm.intercept_)

# 新增係數欄位
coef = pd.DataFrame(california.feature_names, columns=['features'])
coef['estimatedCoefficients'] = lm.coef_  # 新增欄位
print(coef)

# 繪製散佈圖
plt.scatter(x.MedInc, y)
plt.xlabel('medium income in block group(MedInc)')
plt.ylabel('Housing Price(MEDV)')
plt.title('Relationship between MedInc and Price')
plt.show()


#%%
'''
多元線性迴歸:使用加州房價資料集預測房價
4. 使用predict()函數預測房價
'''
# 載入套件&資料集
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 設定資料
california = datasets.fetch_california_housing()

# 建立DataFrame物件
x = pd.DataFrame(california.data, columns=california.feature_names)
target = pd.DataFrame(california.target, columns=['MEDV'])
y = target['MEDV']
# 寫法2: y = pd.DataFrame(california.target, columns=['MEDV'])

# 呼叫fit()函數訓練預測模型
lm = LinearRegression()
lm.fit(x, y)

# 使用predict()函數預測房價
predicted_price = lm.predict(x)
print(predicted_price[0:5])  # 顯示前5筆資料

# 繪製散佈圖比較原本房價和預測房價
plt.scatter(y, predicted_price)
plt.xlabel('Price')
plt.ylabel('Predicted Price')
plt.title('Price vs Predicted Price')
plt.show()

