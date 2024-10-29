# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:10:52 2024

@author: Chang Yen-Yu
"""
#%%
'''
使用fetchall()顯示table01資料表所有資料
每一列資料都是一筆數組資料，可用row[0], row[1]取得資料表前兩個欄位
'''
import sqlite3
conn = sqlite3.connect('test.sqlite')

# 建立cursor物件並顯示
cursor = conn.execute('select * from table01')
print(cursor)
print()

# 從cursor物件取出所有資料，並輸出資料
rows = cursor.fetchall()
print(rows)
print()

# 依序輸出資料
for row in rows:
    print('{:d}\t{:s}'.format(row[0], row[1]))
conn.close()  # 關閉資料庫連線


#%%
'''
使用cursor查詢資料-fetchone()
使用fetchone()顯示table01資料表中'num=1'的第一筆資料
'''
import sqlite3
conn = sqlite3.connect('test.sqlite')

# 建立cursor物件
cur = conn.execute('SELECT * FROM table01 where num=1')

# 從cursor物件中擷取一筆資廖(tuple型態)
row = cur.fetchone()

# 顯示資料
if row != None:
    print('{}\t{}'.format(row[0], row[1]))
    
# 關閉資料連結
conn.close()


#%%
# SQLite3範例1
# 匯入所需套件
import sqlite3

# 建立與test.db連結，若資料庫成功打開，會返回一個連線物件conn
conn = sqlite3.connect('test.db')
print('Openeed database successfully')

# 建立一個cursor物件c
c = conn.cursor()

'''
執行SQL語法建立表格，主鍵為整數型態的ID
欄位有文字型態的NAME，整數型態的AGE，字元型態的ADDRESS，實數型態的SALARY
'''
c.execute('''CREATE TABLE COMPANY
          (ID INT PRIMARY KEY NOT NULL,
           NAME TEXT NOT NULL,
           AGE INT NOT NULL,
           ADDRESS CHAR(50),
           SALARY REAL);''')
print('Table created successfully')

# 確認執行SQL語法與關閉連結資料庫
conn.commit()
conn.close()


#%%
# SQLite3範例2
# 匯入所需套件
import sqlite3

# 建立與test.db的連結，若資料庫成功打開，會返回一個連線物件conn
conn = sqlite3.connect('test.db')

# 建立一個cursor物件c
c = conn.cursor()
print('Opened database successfully')

'''
執行SQL語法建立表格，主鍵為整數型態的ID
欄位有文字型態的NAME，整數型態的AGE，字元型態的ADDRESS，實數型態的SALARY
'''
c.execute('''CREATE TABLE COMPANY
          (ID INT PRIMARY KEY NOT NULL,
           NAME TEXT NOT NULL,
           AGE INT NOT NULL,
           ADDRESS CHAR(50),
           SALARY REAL);''')
print('Table created successfully')

# 執行SQL語法，從COMPANY表新增紀錄
c.execute('INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
          VALUES (1, 'Paul', 32, 'California', 20000.00)');
c.execute('INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
          VALUES (2, 'Allen', 25, 'Texas', 15000.00)');
c.execute('INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
          VALUES (3, 'Teddy', 23, 'Norway', 20000.00)');  
c.execute('INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
          VALUES (4, 'Mark', 25, 'Rich-Mond', 65000.00)');

# 確認執行SQL語法
conn.commit()
print('Records created successfully')

# 關閉連結資料庫
conn.close()

   
#%%
# SQLite3範例3
# 匯入所需套件
import sqlite3

# 建立與test.db的連結，若資料庫成功打開，會返回一個連線物件conn
conn = sqlite3.connect('test.db')

# 建立一個cursor物件c
c = conn.cursor()
print('Opened database successfully')

# 執行SQL語法，從COMPANY表中獲取並顯示紀錄
cursor = c.execute('SELECT id, name, address, salary from company')
for row in cursor:
    print('ID = ', row[0])
    print('Name = ', row[1])
    print('Address = ', row[2])
    print('Salary = ', row[3], '\n')
print('Operation done successfully')
conn.close()


#%%
'''
CSV資料存入SQLite資料庫
'''
import sqlite3

# 將csv字串轉成串列
book = 'P0002,Python程式設計,500'
f = book.split(',')  # 以逗號分隔

# 建立資料庫連接
conn = sqlite3.connect('Books.sqlite')

# 建立SQL指令INSERT字串
sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}','{2}')"
# 使用format()建立SQL語法插入紀錄的SQL語法字串
sql = sql.format(f[0], f[1], f[2])
print(sql)

# 執行SQL指令，呼叫execute()執行新增紀錄
cursor = conn.execute(sql)
# rowcount是影響的紀錄數
print(cursor.rowcount)

# 確認交易，變更資料庫
conn.commit()
# 關閉資料庫連接
conn.close()


#%%
'''
JSON資料存入SQLite資料庫
'''
import sqlites

# 將JSON資料轉成字典(dic)型態
d = {
     'id':'P0003',
     'title':'Node.js程式設計',
     'price':650
     }

# 建立資料庫連接
conn = sqlite3.connect('Books.sqlite')

# 建立SQL指令INSERT字串
sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}','{2}')"
# 使用format()建立SQL語法插入紀錄的SQL語法字串
sql = sql.format(d['id'], d['title'], d['price'])
print(sql)

# 執行SQL指令
cursor = conn.execute(sql)
print(cursor.rowcount)

# 確認交易，變更資料庫
conn.commit()
# 關閉資料庫連接
conn.close()

