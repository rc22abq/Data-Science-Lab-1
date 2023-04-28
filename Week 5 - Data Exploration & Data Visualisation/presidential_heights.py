# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:00:21 2023

@author: jdpev
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print('The heights are as follows:\n', heights)

print("\nThe mean height is as follows: ", heights.mean())
print("The standard deviation is as follows:", heights.std())
print("The minimum height is", heights.min(), 'cm')
print("The maximum height is", heights.max(), 'cm')

print("\n25th percentile: ", np.percentile(heights, 25))
print("Median: ", np.median(heights))
print("75th percentile: ", np.percentile(heights, 75))

plt.style.use('seaborn-whitegrid')
plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')