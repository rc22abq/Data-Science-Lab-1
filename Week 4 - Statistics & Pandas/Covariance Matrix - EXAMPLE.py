# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:14:29 2023

@author: User
"""

# Covariance matrix example

import numpy as np
import scipy.stats as stats


# Samples
x = np.array([92, 60, 100])
y = np.array([80, 30, 70])


#############################################################################


# Calculate the means
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculate the differences
x_diff = x - x_mean
y_diff = y - y_mean

# Length of data
N = len(x)

# Covariance for x,x
covxx = (1/(N-1)) * np.sum(x_diff * x_diff)
print(covxx)

# Covariance for y,y
covyy = (1/(N-1)) * np.sum(y_diff * y_diff)
print(covyy)

# Covariance for y,x
covyx = (1/(N-1)) * np.sum(y_diff * x_diff)
print(covyx)

# Covariance for x,y
covxy = (1/(N-1)) * np.sum(x_diff * y_diff)
print(covxy)


#############################################################################


# Stack these into a 2d array
data = np.vstack((x,y))

# Calculate the covariance matrix
cov = np.cov(data)
print(cov)


#############################################################################


# Pearson's correlation coefficient
print(stats.pearsonr(x,y))