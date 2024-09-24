# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:19:38 2024

@author: Chang Yen-Yu
"""
# 匯入套件
import numpy as np

# 使用numpy隨機產生1-20之間的20個正整數並輸出
ans = []
for i in range(20):
    r = np.random.randint(1, 21)
    ans += [r]
data = np.array(ans)  # 從一維串列轉為一維陣列
print('隨機正整數: ' , data)

# 轉成X矩陣並輸出
x = data.reshape(5, 4)
print('X矩陣內容:', x)

# 輸出X矩陣的最大值
max = x.max()
print('最大:', max)

# 輸出X矩陣的最小值
min = x.min()
print('最小:', min)

# 輸入X矩陣的平均
sum = x.sum()
avg = sum / 20
print('平均:', avg)

# 輸出X矩陣的總和
print('總和:', sum)

# 輸出X矩陣的標準差
std = x.std()
print('標準差:', std)

# 輸出X矩陣四個角落的元素內容
a = x[::4,::3]
print('四個角落元素:', a)

