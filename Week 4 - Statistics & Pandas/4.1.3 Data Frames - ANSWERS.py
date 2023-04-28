# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:50:57 2023

@author: User
"""

import pandas as pd
from pandas import DataFrame
import numpy as np

columns = ['A','B','C','D']
df = pd.DataFrame(np.random.randint(0,10,(100,4)), columns=columns)
print(df)
print(df['A'])
print(df['A']+10) # adds 10 to column A
print(df['A']**2) # squares column A
print(np.sin(df['A'])) # takes sin of column A
print(np.median(df, axis=1))
print(df.describe()) # quick overview of the data frames numbers