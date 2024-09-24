# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:24:27 2024

@author: Chang Yen-Yu
"""
#%%
# ndarray陣列物件相關屬性
import numpy as py
a = np.array([[3,6,9],[2,4,6]])

print('ndim:',a.ndim)  #ndarray有幾維(dimension)
print('shape:',a.shape)  #ndarray的形狀
print('type:',type(a))
print('dtype:',a.dtype)  #ndarray元素的資料型別
print('data:',a.data)  #陣列資料從何處開始(回傳記憶體位置)
print('T/n',a.T,'\n')  #轉置(transform)後的陣列
print(a)
print('size:',a.size)  #ndarray的總元素數量
print('itemsize:',a.itemsize)  #每個元素的記憶體使用量(以byte為單位)
print('nbytes:',a.nbytes)  #ndarray所有元素的記憶體使用量(以byte為單位)

#%%
# Numpy的切割(Slicing)->只改變局部的資料
import numpy as np
arr = np.arange(10)  # arr:0-9
slice = arr[5:8]  #取arr的5,6,7為slice的0,1,2
arr[5:8] = 7  #arr的5-7的value都改為"7"
slice[1] = 87  # slice的1的value改為87

print(slice)
print(arr)

#%%
# Numpy的索引
import numpy as np
x = np.arange(12).reshape(2,6)  #reshape括號內數字相乘一定要等於arange括弧內的數字
print(x)  #[0,1,2,3,4,5][6,7,8,9,10,11]
y = x[1][1:]  #第2個[]內的第2個以後的所有數字:[7,8,9,10,11]
print(y)
y[1] = 200  #y的第2個數字改為200:[7,200,9,10,11]
print(y)
print(x)  #x的數字8也會同步改為200

---
import numpy as np
x = np.arange(12).reshape(3,4)
print(x)
y = x[[0,1,2],[2,1,0]]  # x[row,column]->(0,2),(1,1),(2,0)的values
print(y)

---
# 將格子狀立特定列與特定行交叉點位置的元素取出，使用np.ix函數
import numpy as np
x = np.arange(12).reshape(3,4)
z = x[np.ix_([0,2],[1,3])]  # 用numpy的"ix_"函數->[row,column]->(0,1)(0,3),(2,1)(2,3)的values
print(z)
