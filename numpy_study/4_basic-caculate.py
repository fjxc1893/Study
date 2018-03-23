#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"

import numpy as np
A = np.arange(2, 14).reshape((3, 4))
print(A)
print(np.argmin(A)) #最小值索引
print(np.argmax(A)) #最大值索引
print(np.argmin(A, axis=0)) #最小值按列索引
print(np.mean(A)) #平均值
print(A.mean()) #平均值
print(np.median(A)) #中位数
print(np.cumsum(A))
print(np.nonzero(A)) #会输出“(array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], dtype=int64), array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3], dtype=int64))”
print(np.sort(A))
B = np.arange(14, 2, -1).reshape((3, 4))
print(B)
print(np.sort(B))#矩阵的每一行按顺序排列
print(np.transpose(B)) #矩阵的转置（行列互换）
print(B.T) #效果同上

print(np.clip(B, 5, 9)) #矩阵里小于5都等于5，大于9的都等于9
print(np.mean(B, axis=0)) #对矩阵按列求平均
