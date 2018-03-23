#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"

import numpy as np
A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
C = np.vstack((A, B))
D = np.hstack((A, B))
print(np.vstack((A, B))) #vertical stack 上下合并
print(np.hstack((A, B))) #horizontal stack 水平合并
print(A.shape, C.shape)
print(A.shape, D.shape)
print(A[:, np.newaxis]) #给A在列上加个维度(单行数列转换成纵向的）
E = np.concatenate((A, B, B, A), axis=0)#以增加列的方式合并
print(E)
F = np.vstack((A, B, B, A))
print(F)