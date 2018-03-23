#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"

import numpy as np
a = np.array([2, 23, 4]) #创建一个新的一维数组
print(a) #打印出创建的矩阵 [ 2 23  4]
b = np.array([2, 23, 4], dtype=np.int)
print(b.dtype)
c = np.array([2, 23, 4], dtype=np.float)
print(c.dtype)
d = np.array([[2, 23, 4],
              [2, 3, 4]]) #创建一个新的两行三列的矩阵
print(d)
e = np.zeros((3, 4)) #创建三行四列全部为0的矩阵
print(e)
f = np.ones((3, 4)) #创建三行四列全部为1的矩阵
print(f)
g = np.arange(10, 20, 2) #创建一个从10到19，步长为2的列表
print(g)
h = np.arange(12).reshape((3, 4)) #创建一个从0到11的3行4列矩阵,reshape重新定义长和宽
print(h)
j = np.linspace(1, 10, 20).reshape((4, 5)) #创建一个从1到10，分割为20个元素的4行5列的矩阵
print(j)