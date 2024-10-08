# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:37:05 2024

@author: Chang Yen-Yu
"""
#%%
'''
Questions:
diabetes dataset 是一個糖尿病資料集,主要包括 442 筆資料,10 個屬性值,分別是:age (年齡)、 sex (性別)、
bmi (Body Mass Index 體質指數)、 bp (Average Blood Pressure平均血壓)、s1~s6 (一年後疾病級數指標)。
target 為一年後患疾病的定量指標。
    1. 請建立線性多元迴歸的預測模型,繪出散佈圖來比較預測一年後患疾病的定量指標和實際一年後患疾病的定量指標的結果。
    2. 請建立線性多元迴歸的預測模型,只取 age (年齡)、 sex (性別)、 bmi (Body Mass Index 體質指數)、
bp (Average Blood Pressure 平均血壓) 做為解釋變數,產生模型,並繪出散佈圖來比較預測一年後患疾病的定量指標和
實際一年後患疾病的定量指標的結果。
'''
# Question_1:
    
# 載入套件&資料集
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 設定資料
diabetes = datasets.load_diabetes()

# 建立DataFrame物件
x = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
target = pd.DataFrame(diabetes.target, columns=['MEDV'])
y = target['MEDV']

# 呼叫fit()函數訓練預測模型
lm = LinearRegression()
lm.fit(x, y)

# 新增係數欄位
coef = pd.DataFrame(diabetes.feature_names, columns=['features'])
coef['estimatedCoefficients'] = lm.coef_  # 新增欄位
print(coef)

# 使用predict()函數預測
predict_target = lm.predict(x)
print(predict_target)

# 繪製散佈圖
plt.scatter(y, predict_target)
plt.xlabel('Quantitative Measure')
plt.ylabel('Predicted Quantitative Measure')
plt.title('Quantitative Measure vs Predicted Quantitative Measure')
plt.show()


#%%
# Question_2:

# 載入套件&資料集
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 設定資料
diabetes = datasets.load_diabetes()

# 建立DataFrame物件
x = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
x_select = x.iloc[:, :4]  # rows全部, columns選前4項
target = pd.DataFrame(diabetes.target, columns=['MEDV'])
y = target['MEDV']

# 呼叫fit()函數訓練預測模型
lm = LinearRegression()
lm.fit(x_select, y)

# 使用predict()函數預測
predict_target = lm.predict(x_select)
print(predict_target)

# 繪製散佈圖
plt.scatter(y, predict_target)
plt.xlabel('Quantitative Measure')
plt.ylabel('Predicted Quantitative Measure')
plt.title('Quantitative Measure vs Predicted Quantitative Measure')
plt.show()

