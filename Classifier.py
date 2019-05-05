# -*- coding: utf-8 -*-
"""
Created on Sun May  5 23:01:42 2019

@author: Ahmed
"""

import pandas as pd
df = pd.read_excel("MLDataSet.xlsx")
df2 = pd.read_excel("ADRs.xlsx")
df3 = pd.read_excel("DS.xlsx")
df4 = pd.read_excel("Mental.xlsx")

df5=[df, df2,  df3, df4]

result = pd.concat([df,df2,df3, df4], axis=1, join_axes=[df.index])