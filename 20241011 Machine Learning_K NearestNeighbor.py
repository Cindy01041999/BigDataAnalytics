# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:08:15 2024

@author: Chang Yen-Yu
"""
#%%
'''
K近鄰演算法 K NearestNeighbor
使用K個最接近目標的資料來預測目標所屬的類別
K值須小於樣本數的平方根較好
'''
# Question_1: 分類面紙是好是壞
# 匯入套件
import pandas as pd
import numpy as np
from sklearn import neighbors

x = pd.DataFrame({
    'durability': [7,7,3,1],
    'strength': [7,4,4,4]
})

y = np.array([0,0,1,1])
k = 3  # 鄰近的3個值

# 建立KNeighborsClassifier分類器物件，鄰近k個值
knn = neighbors.KNeighborsClassifier(n_neighbors=k)
# 呼叫fit()函數訓練模型
knn.fit(x, y)

# 預測新產品[3,7]的分類 1:好 0:壞
new_tissue = np.array([[3,7]])
pred = knn.predict(new_tissue)
print(pred)


#%%
# Question_2: 分類鳶尾花
# 使用散佈圖探索鳶尾花資料集

# 匯入套件
import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()

print(iris.DESCR)  # 資料集描述

x = pd.DataFrame(iris.data, columns=iris.feature_names)
x.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']  # 改X欄位名稱
target = pd.DataFrame(iris.target, columns=['target'])
y = target['target']  # target就是資料集裡面的class, 三個類別分別為0,1,2

# 畫散佈圖
colmap = np.array(['r', 'g', 'y']) # red, green, yellow
plt.figure(figsize=(10, 5))  # 設定畫布大小

# 左圖: 花萼長寬
plt.subplot(1, 2, 1)  # 分為1列2欄, 位置在第1欄
plt.subplots_adjust(hspace = .5)  # 座標軸間距為0.5
plt.scatter(x['sepal_length'], x['sepal_width'], color=colmap[y]) # 按照上述colmap設定: y=0為red, y=1為green, y=2為yellow
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

# 右圖: 花瓣長寬
plt.subplot(1, 2, 2)  # 分為1列2欄, 位置在第2欄
plt.scatter(x['petal_length'], x['petal_width'], color=colmap[y])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()

'''
結論:
 左右兩圖相比，右圖(花瓣長寬)可見三個類別分散較為明顯。
 (從iris.DESCR資料集描述中也可見花瓣的長寬 Class Correlation數值較高)
'''    

