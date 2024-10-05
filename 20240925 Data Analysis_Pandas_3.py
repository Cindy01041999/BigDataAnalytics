# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:43:24 2024

@author: Chang Yen-Yu
"""
#%%
# 使用 groupby() 函式進行資料分組
import pandas as pd
col = ['class', 'name', 'bd']
data = [['classA', '小明', '1995-08-01'],
        ['classB', '小美', '1995-10-02'],
        ['classC', '小黃', '1995-06-01'],
        ['classC', '小陳', '1995-10-02'],
        ['classA', '小花', '1995-10-02'],
        ['classB', '小雨', '1995-10-02']]
frame = pd.DataFrame(data, columns = col)  # 將上述list轉為DataFrame資料型態
frame_class = frame.groupby('class')

# 依class進行分組，資料被分成classA, classB, classC，且顯示每個組有什麼資料與資料型態
print(frame_class.groups)

# 取出classA的資料
print(frame_class.get_group('classA'))        


#%%
# 計算分組總和
import numpy as np
import pandas as pd

df = pd.DataFrame(
    {'A':['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
     'B':['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
     'C':np.random.randn(8),
     'D':np.random.randn(8)})
print(df)
print(df.groupby('A').sum())  # 計算總和，以A分組
print(df.groupby(['B','A']).sum())  # 計算總和，先以B分組再以A分組


#%%
# groupby()函式可將資料依照指定欄位分組
import numpy as np
import pandas as pd

df = pd.DataFrame({'Key1':['A','B','A','C','B','D','C','D','A','C'],
                   'Key2':['one','two','one','two','one','two','one','two','one','one'],
                   'data1':np.random.randn(10),
                   'data2':np.random.randn(10)})
print(df)
-----
sector = df.groupby('Key1')  # 以Key1進行分組
print(sector)  # 輸出sector(記憶體位址)
-----
print(type(sector))  # 輸出資料類型
-----
print(sector.size())  # 各組內的個數(A有3個)
-----
print(sector.get_group('A'))  # 取出key1是A的資料
-----
print(sector.get_group('B'))  # 取出key1是B的資料


#%%
'''
使用 to_csv() 將DataFrame物件儲存成CSV檔案。
過程中會將原本的索引當作內容存進去CSV，變成會多一層索引。
'''
import pandas as pd
df = pd.read_csv('nba.csv')  # 讀csv檔
df.to_csv('nba_2.csv')  # 儲存成csv檔

-----
'''
# Solution_1: 不存索引 
df.to_csv(path路徑, index=False/0, header=False/0)
'''
import pandas as pd
df = pd.read_csv('nba.csv')  # 讀csv檔
df.to_csv('nba_2.csv')  # 儲存成csv檔(有多一欄索引)
df.to_csv('nba_3.csv', index=0)  # 不存索引, 沒有多一欄索引
df.to_csv('nba_4.csv', index=0, header=0)  # 不存索引也不存各欄title(header)

-----
'''
# Solution_2: 聲明文件第一列為索引，第一行為欄名
df = pd.read_csv(path, index_col=0, header=0)
'''
import pandas as pd
df = pd.read_csv('nba.csv')
df.to_csv('nba_2.csv') 

df0 = pd.read_csv('nba_2.csv')  # 有多一欄索引欄
df1 = pd.read_csv('nba_2.csv', index_col=0)  # 沒有多一欄索引(實際上還是有，只是沒有顯示出來)
df2 = pd.read_csv('nba_2.csv', index_col=0, header=0)  # 設header=0沒有用，還是會顯示header

# 所以用Solution_1比較好，一開始就不存索引和header


#%%
# 使用Numpy建立資料，並轉成DataFrame後進行繪圖
# 匯入套件
import numpy as np
import pandas as pd

# 建立4個欄位，各100筆隨機資料
x = np.random.rand(100, 4)  # 0-1之間任100筆隨機浮點數
y = np.random.randn(100, 4)  # -3到3之間任100筆隨機數值

# x為日期, columns設定為ABCD
df1 = pd.DataFrame(x, index=pd.date_range('3/1/22', periods=100), columns=list('ABCD'))  # 從2022年3/1開始算100天
df2 = pd.DataFrame(y, index=pd.date_range('3/1/22', periods=100), columns=list('ABCD'))  # 從2022年3/1開始算100天

# 資料未累加時，顯示圖表
df1.plot()  # 4個欄位代表4條線
df2.plot()

# 資料累加後，顯示圖表，使用.cumsum()函式
df1 = df1.cumsum()  # 累加後一定是正數，因為原本是0-1的浮點數
df2 = df2.cumsum()
df1.plot()
df2.plot()


#%%
'''
pandas的plot()函式預設為折線圖
若在plot()裡指定kind引數，可選擇折線圖以外的繪圖格式
'''
# 匯入套件
import pandas as pd
import numpy as np

# 設定DataFrame物件，並進行設定 
# 隨機500筆數字，3個欄位，欄位(線條)名稱為xyz，row資料為從2022/1/1起算500日
df = pd.DataFrame(np.random.randn(500,3), columns=list('xyz'), index=pd.date_range('1/1/2022', periods=500))

# 設定累加
df = df.cumsum()

# 設定折線圖(預設)的設定

# colormap='gray'灰階
df.plot(colormap='gray').set_ylabel('Value', fontsize=12)  # Y軸名稱為Value，字體大小為12

# 長條圖的設定
# 5列3欄，0-1的任意浮點數
df2 = pd.DataFrame(np.random.rand(5, 3), columns=['a','b','c'])

# 設定圖形為長條圖
df2.plot(kind='bar', fontsize=12)
# stacked=True為堆疊圖形
df2.plot(kind='bar', fontsize=12, stacked=True)

