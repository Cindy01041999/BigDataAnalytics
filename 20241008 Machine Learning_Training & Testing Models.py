# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 23:18:59 2024

@author: Chang Yen-Yu
"""
#%%
'''
資料集分割:訓練和測試資料集
使用 train_test_split()函數隨機分割資料集
'''
# 匯入套件及資料集
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
import matplotlib.pyplot as plt

# 建立DataFrame物件
california = datasets.fetch_california_housing()
x = pd.DataFrame(california.data, columns=california.feature_names)
target = pd.DataFrame(california.target, columns=['MEDV'])
y = target['MEDV']

'''
test_size是測試資料集的切割比例, 0.33指測試資料集佔33%, 訓練資料集佔67%
random_state 為隨機數種子，可指定亂數的種子數，保證每次隨機結果都一樣。
'''
xTrain, xTest, yTrain, yTest = tts(x, y, test_size=0.33, random_state=5)


# 呼叫predict()函數使用測試資料集來預測房價
lm = LinearRegression()
lm.fit(xTrain, yTrain)

pred_test = lm.predict(xTest)

# 繪出測試資料集原本房價和預測房價的比較圖
plt.scatter(yTest, pred_test)
plt.xlabel('Price')
plt.ylabel('Predicted Price')
plt.title('Price vs Predicted Price')
plt.show()


#%%
'''
預測模型的績效:
計算 MSE 和 R-squared 來顯示預測模型的績效
'''
# 預測(訓練資料與測試資料集)
pred_train = lm.predict(xTrain)
pred_test = lm.predict(xTest)

# 績效衡量:有MAE、MSE及RMSE，MSE指誤差，其值越小越好
MAE_train = mae(yTrain, pred_train)
MAE_test = mae(yTest, pred_test)
MSE_train = mse(yTrain, pred_train)
MSE_test = mse(yTest, pred_test)

'''
其他寫法:
yTrain, yTest是房價，各自減掉 pre_train和pre_test並進行平方，使用mean()函數計算平均值
# MSE_train = np.mean((yTrain-pred_train)**2)
# MSE_test = np.mean((yTest-pred_test)**2)
'''
RMSE_train = mse(yTrain, pred_train)**0.5
RMSE_test = mse(yTest, pred_test)**0.5

print('訓練資料的MSE:', MSE_train)
print('測試資料的MSE:', MSE_test)

# 績效衡量: R-squared, 指解釋能力，其值越大越好，區間是0~1
# 使用score()函數計算訓練和測試資料的R-squared
print('訓練資料的R-squared:', lm.score(xTrain, yTrain))
print('測試資料的R-squared:', lm.score(xTest, yTest))





