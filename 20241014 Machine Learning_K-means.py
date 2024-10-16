# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:19:51 2024

@author: Chang Yen-Yu
"""
#%%
'''
使用K-means演算法將14隻動物進行分群
指定k值為3, 建立K-means模型
'''

import pandas as pd
import numpy as np
from sklearn import cluster
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Length':[51, 46, 51, 45, 51, 50, 33, 
              38, 37, 33, 33, 21, 23, 24],
    'Weight':[10.2, 8.8, 8.1, 7.7, 9.8, 7.2, 4.8,
              4.6, 3.5, 3.3, 4.3, 2.0, 1.0, 2.0]})
k = 3

# n_clusters是k值, random_state是亂數種子
kmeans = cluster.KMeans(n_clusters=k, random_state=12)
# 呼叫fit()函數訓練模型
kmeans.fit(df)
# labels_顯示分群結果
print(kmeans.labels_)  # 結果是0,1,2
# inertia_計算各樣本到該群中心點距離之平方和，用來評估分群的成效
print(kmeans.inertia_)

# 畫散佈圖
colmap = np.array(['r', 'g', 'y'])  # 設定顏色分別對應kmeans結果0,1,2
# kmeans結果0的顏色是red, 1是green, 2是yellow
plt.scatter(df['Length'], df['Weight'], color=colmap[kmeans.labels_])
plt.show()


#%%
'''
make_blobs()函數 聚類資料生成器
n_samples: 如果是整數->每組的點數總數, 如果是數組->代表每組個數
n_features: 每個樣本的特徵數量
centers: 幾個中心點
cluster_std 參數: 可為每個類別設定不同的標準差
'''
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# 範例一
x, y = make_blobs(n_samples=10, centers=3, n_features=3, random_state=0)
print(x.shape)  # 10列3欄(n_samples=10, 欄位:n_features=3)
print(y)  # 0,1,2(分成3群, 因為中心點centers有3個)
# 畫散佈圖
plt.scatter(x[:,0], x[:,1]) # row全抓，column帶第一和第二欄資料

# 範例二
x2, y2 = make_blobs(n_samples=[3, 3, 4], centers=None, n_features=2, random_state=0)
print(x2.shape)  # 10列2欄(n_samples總共10, 欄位:n_features=2)
print(y2)  # 0,1,2帶入上方n_samples -> 0有3個, 1有3個, 2有4個
plt.scatter(x2[:,0], x2[:,1])  # row全抓，column帶第一和第二欄資料

# 範例三: 生成3類資料, 100個樣本, 每樣本有2個特徵
# 用cluster_std參數為每個類別設定不同的標準差
data, target = make_blobs(n_samples=100, n_features=2, centers=3, cluster_std=[1.0, 3.0, 2.0])
# 在2D圖中，每個樣本顏色不同
plt.scatter(data[:,0], data[:,1], c=target);  # c=colors: 0分一群, 1分一群, 2分一群, 每群不同顏色
plt.show()


#%%
# 範例四
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# 載入scikit-learn資料集範例資料
# 樣本數為200, 分為4群(樣本中心數), 標準差為0.5, 隨機種子為0
x, y = make_blobs(n_samples=200, centers=4, cluster_std=0.50, random_state=0)
plt.scatter(x[:,0], x[:,1])  # 因為沒有設定colors參數, 所以每一群的顏色相同
print(x)


#%%
# 範例五
'''
K-means內的參數, 分群數量(n_clusters)設定為2-10, 初始化(init)設定為'k-means++', 隨機運作次數(n_init)設定為15, 隨機種子為0, 最大迭代次數(max_iter)設定為200
使用集群內誤差平方和(inertia_)判斷分群數量, 取值<100納入計算，可看到分為7組
'''
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# 載入scikit-learn資料集範例資料
x, y = make_blobs(n_samples=200, centers=4, cluster_std=0.50, random_state=0)
plt.scatter(x[:,0], x[:,1])
print(x)

# 假設分成2-10組, 看哪一組的inertia最小
data = {}
for i in range(2, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=200, n_init=15, random_state=0)
    kmeans.fit(x)
    if kmeans.inertia_ < 100:
        data[i] = kmeans.inertia_
        
print('inertia_ < 100 的總共有:', len(data), '組')
print('inertia 最小值為:', min(data.values()))


#%%
# 範例六
'''
假設n_clusters設定為7個分群, 看一下最小中心點x的位置和最大中心點y的位置
'''
kmeans = KMeans(n_clusters=7, init='k-means++', max_iter=200, n_init=15, random_state=0)
kmeans_fit = kmeans.fit(x)
kmeans_predict = kmeans_fit.predict(x)
# 另一種方式: kmeans_predict = kmeans.fit_predict(x)

print('cluster_centers = ', kmeans.cluster_centers_) # 列出7群各自的中心點
print('Min:', min(kmeans.cluster_centers_[:,0].round(4)), sep='')  # 最小中心點
print('Max:', max(kmeans.cluster_centers_[:,1].round(4)), sep='')  # 最大中心點
# print('Min:{:.4f}'.format(min(kmeans.cluster_centers_[:,0])))
# print('Max:{:.4f}'.format(max(kmeans.cluster_centers_[:,1])))


#%%
'''
建立K-means模型分群鳶尾花
K-means是非監督式學習，只需資料集x即可，不需要答案的標籤y
變數y的目的只是驗證分群結果
'''
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import cluster
import matplotlib.pyplot as plt

# 載入Iris資料
iris = datasets.load_iris()

# 建立DataFrame物件x
x = pd.DataFrame(iris.data, columns=iris.feature_names)
# 欄位名稱更改 -> 去除掉cm
x.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
y = iris.target
k = 3  # 變數k值設定為3

# 分為k群(3群), 亂數種子為12
kmeans = cluster.KMeans(n_clusters=k, random_state=12, n_init='auto')
# fit()訓練模型
kmeans.fit(x)
# 輸出kmeans結果
print(kmeans.labels_)  # kmeans預測結果 -> [0,2,1]
print(y)  # y為實際結果(用來驗證預測準確性) -> [0,1,2]


# 畫散佈圖來比較kmeans預測結果和y實際結果
# y實際結果的散佈圖
colmap = np.array(['r', 'g', 'y'])  # 設定顏色
plt.figure(figsize = (10, 5))  # 設定畫布大小
plt.subplot(121)  # 分為1列2欄，在第1欄
plt.scatter(x['petal_length'], x['petal_width'], color=colmap[y])  # 散佈圖X軸和Y軸資料，分群0,1,2分別對應顏色red, green, yellow
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Real Classification')

# kmeans預測結果的散佈圖
plt.subplot(122)
plt.scatter(x['petal_length'], x['petal_width'], color=colmap[kmeans.labels_])  # 分群0,2,1分別對應顏色red, green, yellow
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('K-means Classification')
plt.show()

'''
由上述兩張散佈圖可見，綠色和黃色的點分布相反，因為kmeans預測結果是[0,2,1]，但y實際結果是[0,1,2]
因此需要修正顏色標籤錯誤:使用Numpy的choose()函數來更改
np.choose(欲修改的資料, 修正對應的清單)
'''

# 修正標籤錯誤
pred_y = np.choose(kmeans.labels_, [0,2,1])  # 從[0,1,2] -> [0,2,1]
print('K-means Fix Classification:')
print(pred_y)
print('Real Classification:')
print(y)


#%%
'''
K-means模型的績效測量:
先匯入metrics物件，使用準確度(Accuracy)和混淆矩陣(Confusion Matrix)來進行模型的績效測量。
accuracy_score(真實的分類值, 模型的分類值)
'''
import sklearn.metrics as sm
# 績效矩陣
print(sm.accuracy_score(y, pred_y))  # 準確率高達約89%
# 混淆矩陣
print(sm.confusion_matrix(y, pred_y))  # 從矩陣可看出對的數量和錯的數量

