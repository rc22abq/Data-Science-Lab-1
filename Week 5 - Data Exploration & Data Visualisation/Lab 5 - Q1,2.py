# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:35:14 2023

@author: User
"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

# Creates plot and axis
fig = plt.figure()
ax = plt.axes()
#plt.xlim(0, 8)
#plt.ylim(0, 8)

# Loads csv file
data = pd.read_csv("president_heights.csv")

# maximum height, minimum height, mean height and standard deviation
# 25th percentile, median and 75th percentile
print(data['height(cm)'].describe())

# Histogram of data
data['height(cm)'].plot(kind='hist')

