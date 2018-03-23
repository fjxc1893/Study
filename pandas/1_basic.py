#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"

import pandas as pd
import numpy as np
s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)
dates = pd.date_range('20180315', periods=6)
print (dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates,columns=("a", "b", "c", "d") )
print (df)
df1 = pd.DataFrame(np.random.randn(6,6))
print (df1)
df2 = pd.DataFrame(np.arange(12).reshape(3,4))
print (df2)
df3 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20180315'), 'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df3)
print(df3.dtypes)
print(df3.index)
print(df3.columns)
print(df3.values)
print(df3.describe())
print(df3.T)
print(df3.sort_index(axis=1, ascending=False))
print(df3.sort_index(axis=0,ascending=False))
print(df3.sort_values(by='E'))