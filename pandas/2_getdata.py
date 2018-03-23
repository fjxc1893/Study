#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"
import numpy as np
import pandas as pd
dates = pd.date_range('20180315', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=("A", "B", "C", "D"))
print(df)
print(df['A'], df.A)
print(df[0:3], df['20180315':'20180317'])

#select by label : loc
print(df.loc['20180315'])
print(df.loc['20180316', ['A', 'B']])
#select by position :iloc
print(df.iloc[[1, 3, 5], 1:3])
#mixed selection :ix
print(df.ix[:3, ['A', 'C']])

#Boolean indexing
print(df)
print(df[df.A > 8])
print(df[df.A < 8])