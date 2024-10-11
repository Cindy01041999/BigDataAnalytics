# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:51:08 2024

@author: Chang Yen-Yu
"""
#%%
'''
決策樹 Decision Tree
使用決策樹分類鳶尾花
'''
from sklearn import datasets

iris = datasets.load_iris()
print(iris.keys())
print(iris.data.shape)
print(iris.feature_names)  # 特徵名稱
print(iris.DESCR)  # 資料集描述


#%%
import pandas as pd
from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

iris = datasets.load_iris()

x = pd.DataFrame(iris.data, columns=iris.feature_names)
target = pd.DataFrame(iris.target, columns=['iris_type'])
y = target['iris_type']

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.33, random_state=1)

dtree = tree.DecisionTreeClassifier()  # tree模組內的決策樹分類器
dtree.fit(xTrain, yTrain)  # 訓練模型

print('準確率:', dtree.score(xTest, yTest))
print(dtree.predict(xTest))
print(yTest.values)

# 畫圖
fig = plt.figure(figsize=(25,20))  # 設定畫布大小
# 匯入tree套件內的plot_tree函數來畫圖
tree.plot_tree(dtree, feature_names=iris.feature_names, class_names=list(iris.target_names), filled=True)  # filled=True代表顏色填滿
fig.savefig('iris.png')  # 圖片存檔


