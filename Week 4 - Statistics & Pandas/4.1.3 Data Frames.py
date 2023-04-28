# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:42:59 2023

@author: User
"""

# 4.1.3 Data Frames

import pandas as pd
from pandas import DataFrame
import numpy as np

# Creating a series
series_dict = {'0':234567,'1':7385,'2':648538,'3':35486}
series = pd.Series(series_dict)
print(series)

print('\n')

# Creating a data frame
data_frame = {'univerisity':['UCL','KCL','UH','Imperial'],
              'pop':[234567,7385,648538,35486]}
unidata = DataFrame(data_frame)
print(unidata)