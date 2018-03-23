#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"

import numpy as np

A = np.arange(12).reshape((3,4))
print(A)
B = np.split(A, 2, axis=1) #按列将矩阵分成2等分
print(B)
C = np.split(A, 3, axis=0) #按行将矩阵分成3等分
print(C)
D = np.array_split(A, 3, axis=1) #按列将矩阵分成3份
print(D)
print(np.vsplit(A, 3))#纵向分割成3等份
print(np.hsplit(A, 2))#横向分割成2等份，如果不能等分则会报错