#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"

import numpy as np
a = np.arange(4)
print(a)
b = a
c = a
d = b
a[0] = 11
print(b, c, d)
print(a, b, c, d)
d[1:3] = [22, 33]
print(a, b, c, d)
b = a.copy() #深度copy 改变a不会影响到b
a[3] = 44
print(a, b, c, d)


