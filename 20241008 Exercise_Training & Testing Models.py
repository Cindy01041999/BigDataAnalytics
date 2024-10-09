# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 01:12:28 2024

@author: Chang Yen-Yu
"""
#%%
'''
Questions:
接續diabetes dataset資料集，進行以下流程:
1. 不分割資料集，請求出MSE及R**2
2. 請分割成訓練資料集及測試資料集的比率為3:1, 亂數種子為100, 求出MSE及R**2?
3. 請分割成訓練資料集及測試資料集的比率為4:1, 亂數種子為100, 求出MSE及R**2?
4. 請問您會選擇以上1,2,3哪種方式建立模型? Why?
'''
# Question_1:不分割資料集，請求出MSE及R**2
# 匯入套件和資料集
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
import matplotlib.pyplot as plt

diabetes = datasets.load_diabetes()

# 建立DataFrame物件
x = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
target = pd.DataFrame(diabetes.target, columns=['MEDV'])
y = target['MEDV']

# 呼叫fit()函數訓練預測模型
lm = LinearRegression()
lm.fit(x, y)

# 預測y值
predict_y = lm.predict(x)

# 計算MAE和MSE
MAE = mae(y, predict_y)
MSE = mse(y, predict_y)

print('不分割資料集 MSE:', MSE)
print('不分割資料集 R-squared:', lm.score(x, y))


#%%
# Question_2:分割成訓練資料集及測試資料集的比率為3:1, 亂數種子為100, 求出MSE及R**2
# 匯入套件和資料集
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
import matplotlib.pyplot as plt

diabetes = datasets.load_diabetes()

# 建立DataFrame物件
x = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
target = pd.DataFrame(diabetes.target, columns=['MEDV'])
y = target['MEDV']

# 訓練資料集及測試資料集的比率為3:1, 亂數種子為100
xTrain, xTest, yTrain, yTest = tts(x, y, test_size=0.25, random_state=100)

# 呼叫fit()函數訓練預測模型
lm = LinearRegression()
lm.fit(xTrain, yTrain)

# 預測y值
pred_train = lm.predict(xTrain)
pred_test = lm.predict(xTest)

# 計算MSE
MSE_train = mse(yTrain, pred_train)
MSE_test = mse(yTest, pred_test)

print('訓練資料MSE:', MSE_train)
print('測試資料MSE:', MSE_test)

print('訓練資料R-squared:', lm.score(xTrain, yTrain))
print('測試資料R-squared:', lm.score(xTest, yTest))


#%%
# Question_3:分割成訓練資料集及測試資料集的比率為4:1, 亂數種子為100, 求出MSE及R**2?
# 匯入套件和資料集
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
import matplotlib.pyplot as plt

diabetes = datasets.load_diabetes()

# 建立DataFrame物件
x = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
target = pd.DataFrame(diabetes.target, columns=['MEDV'])
y = target['MEDV']

# 訓練資料集及測試資料集的比率為4:1, 亂數種子為100
xTrain, xTest, yTrain, yTest = tts(x, y, test_size=0.2, random_state=100)

# 呼叫fit()函數訓練預測模型
lm = LinearRegression()
lm.fit(xTrain, yTrain)

# 預測y值
pred_train = lm.predict(xTrain)
pred_test = lm.predict(xTest)

# 計算MSE
MSE_train = mse(yTrain, pred_train)
MSE_test = mse(yTest, pred_test)

print('訓練資料MSE:', MSE_train)
print('測試資料MSE:', MSE_test)

print('訓練資料R-squared:', lm.score(xTrain, yTrain))
print('測試資料R-squared:', lm.score(xTest, yTest))


#%%
# Question_4:請問您會選擇以上1,2,3哪種方式建立模型? Why?
# Answer_4:
print('會選擇第2種方法(3:1), 因為以上幾種方式的績效差不多，但第2種方式的成本較低(花75%訓練, 25%測試)')

