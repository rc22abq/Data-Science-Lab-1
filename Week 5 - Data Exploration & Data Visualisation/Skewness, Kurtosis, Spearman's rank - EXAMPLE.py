# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:51:02 2023

@author: User
"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

sample = np.random.normal(0,1,1000)
sample2 = np.random.normal(1,2,1000)

# Skewness and Kurtosis
print(stats.skew(sample),stats.kurtosis(sample))

plt.figure()
plt.hist(sample)
plt.hist(sample2,alpha=0.5)
plt.show()

# Spearman's rank
r,p = stats.spearmanr(sample,sample2)
print(r,p)
