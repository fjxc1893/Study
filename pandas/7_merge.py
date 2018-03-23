#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"

import pandas as pd

##merging two df by key/keys.(may be used in database0
##simple example
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
res = pd.merge(left, right, on='key')
print(res)
#consider two keys
left1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right1 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                     'key2': ['K0', 'K0', 'K0', 'K0'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})
print(left1)
print(right1)
res1 = pd.merge(left1, right1, on=['key1', 'key2'], how='inner')
#how = 'inner' 'outer' 'left' 'right'
print(res1)
#indicator
df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
print(df1)
print(df2)
res2 = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print(res2)
#merged by index
left2 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                     'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
print(left2)
print(right2)
#left_index and right_index
res3 = pd.merge(left2, right2, left_index=True, right_index=True, how='outer')
res4 = pd.merge(left2, right2, left_index=True, right_index=True, how='inner')
print(res3)
print(res4)
#handle overlapping
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res5 = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(boys)
print(girls)
print(res5)

#join
