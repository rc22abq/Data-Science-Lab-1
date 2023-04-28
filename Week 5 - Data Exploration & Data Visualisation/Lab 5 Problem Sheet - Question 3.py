# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:49:39 2023

@author: User
"""

import numpy as np
import pandas as pd
from pandas import Series

s = Series([42, 48, 24, 25, 42, 28, 31, 33, 51, 57, 68, 33, 75, 36, 79, 85, 79])

print("Series, s =\n", s, "\n")

print("Median =", np.mean(s))

iqr = np.percentile(s,75) - np.percentile(s,25)
print("\nIQR height =", iqr)

ADD = (1/len(s)) * np.sum(np.abs(s - np.mean(s)))
print("\nAAD =", ADD)

MAD = np.median(np.abs(s - np.mean(s)))
print("\nMAD =", MAD)

print("\nVariance =", np.var(s))

print("\nStandard deviation =", np.std(s))