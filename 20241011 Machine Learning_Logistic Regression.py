# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:01:21 2024

@author: Chang Yen-Yu
"""
#%%
'''
鐵達尼號生存預測:使用邏輯迴歸進行預測
'''
# 載入套件
import pandas as pd
import numpy as np
from sklearn import preprocessing, linear_model

# 匯入csv資料
titanic = pd.read_csv('titanic.csv')
print('原始資料')
titanic.info()

'''
問題:
    1.PClass乘客等級不是數值資料 -> 需轉為數值
    2.Age欄位有遺漏值(NaN) -> 填入中位數
以上問題要先處理完才能訓練預測模型
'''

# 將年齡的空值填入年齡的中位數
age_median = np.nanmedian(titanic['Age'])
print()
print('年齡中位數', age_median)
print()
new_age = np.where(titanic['Age'].isnull(), age_median, titanic['Age'])
titanic['Age'] = new_age

# 更新後資料
print('更新後資料')
titanic.info()

# 欄位轉換為數值
'''
因PClass欄位不是數值，需轉換欄位值成為數值:
1.使用scikit-learn套件中的LabelEncoder()函數建立物件
2.呼叫fit_transform()函數將分類字串轉成數值，將PClass欄位的'1st','2nd','3rd'轉換為數值，就可建立x和y
'''
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic['PClass'])

x = pd.DataFrame([encoded_class, titanic['SexCode'], titanic['Age']]).T  # .T欄列轉換
y = titanic['Survived']

# 程式碼建立LogisticRegression物件logistic後，呼叫fit()函數訓練模型
logistic = linear_model.LogisticRegression()
logistic.fit(x, y)

# 顯示迴歸係數和截距
print('迴歸係數:', logistic.coef_)
print('截距:', logistic.intercept_)

# 混淆矩陣
'''
1.使用predict()函數進行訓練資料集的生存預測
2.使用crosstab()函數建立交叉分析表
'''
print('混淆矩陣')
preds = logistic.predict(x)
print(pd.crosstab(titanic['Survived'], preds))
# 只有斜對角805, 265是True(預測正確)

# 計算邏輯迴歸預測模型的準確度
'''
1.預測正確人數除以全部人數
2.呼叫score()函數計算正確率
'''
print((805+265)/(805+58+185+265)) 
print(logistic.score(x, y))


