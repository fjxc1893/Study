#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"

import numpy as np
array = np.array([[1, 2, 3],
                 [2, 3, 4]])
print(array)
print('number of dim:', array.ndim) #打印出维度 number of dim: 2
print('shape:', array.shape) #打印出数组（矩阵）的行、列数 shape: (2, 3)
print('size:', array.size) #打印出数组中元素的个数 size: 6

