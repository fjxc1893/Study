#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"

import numpy as np

A = np.arange(3, 15)
print(A)
print(A[3])

B = np.arange(3, 15).reshape((3, 4))
print(B)
print(B[2]) #默认索引行（第3行，从0开始）
print(B[2][1])#索引第3行第2列
print(B[2, 1])#效果同上
print(B[:, 2]) #第3列

for row in B:
    print(row)# 迭代行，循环2次

for column in B.T:
    print(column) #迭代列

print(B.flatten()) #将矩阵转换成一行的序列
for item in A.flat:
    print(item) # 迭代每个元素，每个元素占一行