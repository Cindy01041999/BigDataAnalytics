# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:55:08 2024

@author: Chang Yen-Yu
"""
#%%
'''
Questions:
NBApoints.csv 收集 NBA 球員的資訊共 30 個欄位，資料集欄位簡易說明如下，其餘省略。
請進行以下處理：
1. 請將 Pos 欄位及 Tm 欄位資料轉換為數值型態。(Hint: LabelEncoder())
2. 接著用線性迴歸，以 Pos、Age、Tm 三個欄位進行訓練建立模型。
3. 請輸入測試資料[5,28,10]，預測 NBA 球員的三分球得球數，輸出到小數點後第四位。
4. 請計算出 MAE、MSE、RMSE、R-squared。
'''
# Question_1:請將 Pos 欄位及 Tm 欄位資料轉換為數值型態。(Hint: LabelEncoder())
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae

data = pd.read_csv('NBApoints.csv')

labelencoder = LabelEnoder()

# 將 Pos 欄位及 Tm 欄位資料轉換為數值型態
PosToDigit = labelencoder.fit_transform(data['Pos'])
TmToDigit = labelencoder.fit_transform(data['Tm'])


#%%
# Question_2:用線性迴歸，以 Pos、Age、Tm 三個欄位進行訓練建立模型
x = pd.DataFrame([PosToDigit, data['Age'], TmToDigit]).T
x.columns = ['Pos', 'Age', 'Tm']
y = data['3P']

# 訓練模型
lm = LinearRegression()
lm.fit(x, y)


#%%
# Question_3:輸入測試資料[5,28,10]，預測 NBA 球員的三分球得球數，輸出到小數點後第四位
pred = lm.predict([[5,28,10]])
print(f'三分球得球數: {pred[0]:.4f}')  # 變為一維陣列


#%%
# Question_4:請算出MAE、MSE、RMSE、R-squared
pred_y = lm.predict(x)
print('MAE:', mae(y, pred_y))
print('MSE:', mse(y, pred_y))
print('RMSE:', mse(y, pred_y) ** 0.5)
print('R-squared:', lm.score(x, y))

