#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"

import numpy as np
import pandas as pd

# concatenating
df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])
print(df1)
print(df2)
print(df3)
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)

#jion,['inner', 'outer']
df4 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'])
res1 = pd.concat([df1, df2], join='outer', ignore_index=True)
print(res1)
res2 = pd.concat([df1, df2], join='inner', ignore_index=True)
print(res2)

#jion_axes
res3 = pd.concat([df1, df4], axis=1, join_axes=[df1.index])
print(res3)

#append
res4 = df1.append([df3, df2], ignore_index=True )
print(res4)
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s1)
res5 = df1.append(s1, ignore_index=True)
print(res5)