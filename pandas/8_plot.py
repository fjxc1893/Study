#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##plot data

#Series
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()
data.plot()
#plt.show()
#DataFrame
data1 = pd.DataFrame(np.random.randn(1000, 4), index=np.arange((1000)),columns=list("ABCD"))
data1 = data1.cumsum()
print(data1.head(10))
#plot methods
# 'bar' 'hist' 'box' 'kde' 'area'
ax = data1.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1')#some canshu can be used
data1.plot.scatter(x='A', y='C', color='DarkGreen', label='Class 2', ax=ax)
plt.show()