# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:26:33 2024

@author: Chang Yen-Yu
"""
#%%
# 資料篩選-運算子應用(>,<,==,!=,>=)
import pandas as pd

'''
有時資料不會完整顯示(以"..."表示)，若需要顯示所有列/欄 -> 使用.set_option()函式
    1.所有列: set_option('display.max_rows', None)
    2.所有欄: set_option('display.max_rows', None)
'''
# 顯示所有列
pd.set_option('display.max_rows', None)  # None代表"all", 若None改為數字5, 則僅顯示5列資料
# 顯示所有行
pd.set_option('display.max_rows', None)  # None代表"all", 若None改為數字5, 則僅顯示5列資料

df = pd.read_csv('nba.csv')  # 讀取csv檔案
print(df['Age'] >= 25)  # 年紀是否大於等於25?是->True, 否->False

mask = (df['Age'] >= 25)
print(df[mask].head(8))  # 在年紀>=25的條件下, 顯示前8筆

mask1 = (df['Age'] < 29)  # 年紀<29的資料
print(df[mask & mask1].head(8))  # 在年紀25<=age<29的條件下, 顯示前8筆


#%%
# 資料篩選-使用.between()函式取中間範圍的資料
import pandas as pd
df = pd.read_csv('nba.csv')  # 讀取csv檔

# 使用between(20,28)取20-28之間的數值
mask1 = df['Age'].between(20,28)
print(df[mask1].head(8))  # 在20-28歲的條件下, 顯示前8筆


#%%
# 資料篩選-使用函式.isin()篩選符合特定值的資料
import pandas as pd
df = pd.read_csv('nba.csv')

# 使用函式.isin()篩選
mask1 = df['Age'].isin([25,28,32])  # 篩選年紀為25,28,32的資料
print(df[mask1].head(8))  # 在年紀為25,28,32的條件下, 顯示前8筆資料
print(df[mask1].values[:10])  # 在年紀為25,28,32的條件下, 顯示前10筆資料的values
print(df[mask1].index.values[:10])  # 在年紀為25,28,32的條件下, 顯示前10筆的index numbers


#%%
'''
進階資料選擇 -> loc索引: (非函式)
以row(列)標籤和column(欄)標籤的名稱進行資料擷取
先列後欄, 中間用逗號分割
'''
# 使用numpy的亂數函式產生隨機數字，並轉換成DataFrame資料型態
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(5,3),\
                  index=list('ABCDE'),columns=list('XYZ'))
print(df)

# loc索引
print(df.loc['A', 'X'])  # 顯示A列X欄的資料
print(df.loc['B':'D',:])  # 顯示B列到D列的所有欄資料
print(df.loc[:,'X':'Y'])  # 顯示X欄到Y欄的所有列資料
print(df.loc['A':'C','X':'Y'])  # 顯示A列到C列，X欄到Y欄的資料
print(df.loc[['B','E'],['X','Z']])  # 顯示B列、E列且X欄、Z欄的資料


#%%
'''
進階資料選擇 -> iloc索引: (非函式)
以列索引和欄索引(index, columns)，都是從0開始(若索引為ABC->此非索引,僅為代名稱,索引仍為數字)
先列後欄, 中間用逗號分割 (若為[數字:數字]-> 包前不包後)
'''
# 使用numpy的亂數函式產生隨機數字，並轉換成DataFrame資料型態
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.rand(3,3),\
                  index=list('xyz'),columns=list('XYZ'))
print(frame)

# iloc索引
print(frame.iloc[0,0])  # 列索引=0且欄索引=0的值
print(frame.iloc[0:2,:])  # 列索引為0-1, 所有欄的值
print(frame.iloc[:,0:2])  # 所有列, 欄索引為0-1的值
print(frame.iloc[0:2,0:2]) # 列索引0-1, 欄索引0-1的值
print(frame.iloc[[0,2],[0,2]])  # 列索引為0和2, 欄索引為0和2的值

