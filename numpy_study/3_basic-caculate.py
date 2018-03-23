#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"

import numpy as np
a = np.array([10, 20, 30, 40])
b = np.arange(4)
print(a, b)
c = a+b
print(c)
d = a-b
print(d)
e = b**2
print(e)
print(b < 3)
print(b ==3)
aa = np.array([[1, 1],
               [0, 1]])
bb = np.arange(4).reshape((2,2))
print(aa)
print(bb)
cc = aa*bb #普通运算
c_dot = np.dot(aa, bb) # 矩阵运算
print(cc)
print(c_dot)
ran = np.random.random((2,4))
print(ran)
print(np.sum(ran))
print(np.min(ran))
print(np.max(ran))
print(np.sum(ran, axis=1)) #axis=1 表示在行上运算
print(np.min(ran, axis=0)) #axis=0 表示在列上运算
print(np.max(ran, axis=1))