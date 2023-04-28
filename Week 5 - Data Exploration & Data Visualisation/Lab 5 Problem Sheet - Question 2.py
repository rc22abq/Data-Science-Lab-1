# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:26:09 2023

@author: User
"""

# Lab 5 Problem Sheet
# Question 2

import numpy as np
import pandas as pd
from pandas import DataFrame
from scipy import stats

dam = {"dam":["Oroville Dam", "Hoover Dam", "Glen Canyon Dam", "Don Pedro Dam", "Hungry Horse Dam", "Round Butte Dam", "Pine Flat Lake Dam"],
       "height":[756, 726, 710, 568, 564, 440, 440]}
damData = DataFrame(dam)
damData

print("Mean height =", np.mean(damData["height"]))
print("Median height =", np.median(damData["height"]))
print("Mode height =", stats.mode(damData["height"]))

iqr = np.percentile(damData["height"],75) - np.percentile(damData["height"],25)
print("IQR height =", iqr)

print("Variance height =", np.var(damData["height"]))
print("Standard deviation height =", np.std(damData["height"]))

variance = (np.std(damData["height"])) * (np.std(damData["height"]))
print("Variance height =", variance)

