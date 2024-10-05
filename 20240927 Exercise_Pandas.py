# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 18:09:21 2024

@author: Chang Yen-Yu
"""
#%%
'''
1.將行標題設為國文、英文、數學、社會、自然，列標題為個人名字。
'''
import pandas as pd
data = {'國文': [75, 91, 71, 69],
        '數學': [62, 53, 88, 53],
        '英文': [85, 56, 51, 87],
        '自然': [73, 63, 69, 74],
        '社會': [60, 65, 87, 70]}

df = pd.DataFrame(data, index=['小林', '小黃', '小陳', '小美'])

print(df)


#%%
'''
2.輸出後二位學生的所有成績
'''
print('後二位的成績:')
print(df.tail(2))


#%%
'''
3.將自然成績做遞減排序輸出
'''
print('以自然遞減排序:')
print(df['自然'].sort_values(ascending=False))


#%%
'''
4.僅列小黃的成績，並將其英文成績改為80
'''
df.loc['小黃','英文'] = 80
print('小黃的成績:')
print(df.loc['小黃',:]) # 列為小黃，欄為全部成績

