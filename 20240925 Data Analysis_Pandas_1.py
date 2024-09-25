# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:15:28 2024

@author: Chang Yen-Yu
"""
#%%
# index不一定要從0開始，也可以是其他內容
import pandas as pd
ss1 = pd.Series([4, 7, -5, 3], index = ['a', 'b', 'c', 'd'])

print(ss1.index)  # ss1的索引資料
print(ss1['a'])  # 索引'a'的內容
print('a' in ss1)  # 索引'a'有沒有在ss1中
print(7 in ss1)  # 索引7有沒有在ss1中
print(7 in ss1.values)  # 內容7有沒有在ss1中


#%%
# 串列(list)或字典(dict)轉換成Series資料型態
import pandas as pd

# list轉成Series
list_ex = ['A', 123, 'B', 4.56, 'C', True]  #list資料型態
list_to_Series = pd.Series(list_ex)
print(list_to_Series)

# dict轉成Series
dic_ex = {'A':123, 'B':4.56, 'C':True}
dic_to_Series = pd.Series(dic_ex)
print(dic_to_Series)


#%%
# 使用DataDrame()函式將dict資料型態的data轉成dataframe的格式
import pandas as pd
data = {'name':['Bob', 'Nancy'], 'year':[1996, 1997], 'month':[8, 1]}
df = pd.DataFrame(data)
print(df)
print('-----------')  # 用虛線隔開

'''
若要調整欄位順序，可在DataFrame函式中設定columns參數，也可以針對index做設定
# 若columns沒有對應欄位，就會產生新欄位，內容為NaN(例如底下的'ABC'沒有在上方data中定義)
'''
df1 = pd.DataFrame(data, columns = ['name', 'day', 'month', 'year', 'ABC'], index = ['a', 'b'])
print(df1)


#%%
# 資料選擇查詢->自行建立dataframe查詢資料
import pandas as pd
x = [['Amy', 'F', 80], ['Bob', 'M', 65], ['Cindy', 'F', 73], ['Dave', 'M', 46], ['Eva', 'F', 46]]
df1 = pd.DataFrame(x, columns = ['name', 'gender', 'mathgrade'])

print('-----顯示資料一--索引方式-----')
print(df1['name'])  # 用欄名稱，顯示這一欄的index名稱、內容及資料型態
print(df1['name'].values)  # 用欄名稱，僅顯示內容

print(df1['name'][1])  # 用欄列名稱，先欄再列，且僅顯示內容
print(df1['name'][1].value)  # 無法執行->用[1]即可顯示Name欄位的values, 不需要再額外加上'.value'


#%%
# Dataframe屬性
# 使用read()函式讀取檔案
import pandas as pd
df = pd.read_csv('csvsample.csv')  # 讀取csv檔
print(df.nim)  # ndim:幾維
print('---')  # 分隔線
print(df.shape)  # 欄列個數(rows, column)
print('---')
print(df.types)  # 資料類型
print('---')


#%%
'''
Dataframe函式:
    1.head(): 前幾筆資料，若括號內沒填入數字，預設顯示前5筆資料
    2.tail(): 後幾筆資料，若括號內沒填入數字，預設顯示最後5筆資料
    3.info(): 檔案資訊，含欄位名稱、筆數、大小、資料類型
'''
import pandas as pd
df = pd.read_csv('csvsample.csv')
print(df.head(6))  # 顯示前6筆資料
print('---')  # 分隔線
print(df.tail(3))  # 顯示最後3筆
print('---')
print(df.info())  # 檔案資訊


#%%
# 資料選擇查詢-讀取資料進行查詢

# 讀取檔案
df = pd.read_csv('nba.csv')

# 選擇顯示Name欄位資料
print(df['Name'])

# 先挑出Name這個column的所有資料，再選擇特定索引值的資料(先column, 再index)
print(df['Name'][0:6])  # 選index:0-5的資料
print(df['Name', 'Team'].head(10))  # 選擇多項資料，顯示前10筆


#%%
# 新增/刪除資料
'''
使用insert()函式新增資料:
    insert(索引位置, column名稱, 預設值value)
'''
# 新增資料(欄位)
df.insert(1, column='Sport', value='checked')  # 在index=1這一欄(垂直的)新增Sport欄位，且欄位的value都是'checked'
print(df.head())  # 顯示前5筆資料(head函式預設顯示前5筆)

'''
使用drop()函式刪除欄位/資料: axis=0代表刪除筆數(row)(刪除列), axis=1代表刪除欄位(column)(刪除欄)
    1.刪除欄位: drop(要刪除的欄位, axis=1)
    2.刪除資料: drop(要刪除的index number, axis=0)
'''
# 刪除欄位
df = df.drop('Sports', axis=1)  # 刪除Sports這一欄位
print(df.head())  # 顯示前5筆資料(head函式預設顯示前5筆)
print('---')  # 分隔線

# 刪除資料
df = df.drop(0, axis=0)  # 刪除index=0的這一列
print(df.head())  # 顯示前5筆資料(因為index=0已被刪除，所以剩下的index排列是index=1-5)

'''
遺漏值(NaN)的處理:
1. 使用dropna()刪除空的資料(顯示NaN的):
    若是特定欄位的空值才要刪除，在dropna()函式中加入參數subset設定:
        dropna(subset=['欄位名稱1', '欄位名稱2'])
2. 使用fillna()將空資料(NaN)填補代換掉=>在()內輸入替代值
'''
import pandas as pd
df = pd.read_csv('nba.csv')
print(df.head())

# 填入空資料
df = df.fillna(10000)
print(df.head())


#%%
# 資料排序
'''
使用.sort_values()進行資料排序->在()內輸入要排序的column
若排序想反過來，在()內加入ascending設定為False
'''
import pandas as pd
df = pd.read_csv('nba.csv')
print(df.head(6))  # 顯示前6筆
print(df.sort_values('Age'.head(6)))  # 按照Age欄做排序，並顯示前6筆
print(df.sort_values('Name', ascending=False).head(6))  # 按照Age欄做倒序(反過來排序)，並顯示前6筆

