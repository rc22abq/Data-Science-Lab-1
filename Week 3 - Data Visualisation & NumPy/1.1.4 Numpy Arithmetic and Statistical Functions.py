# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:54:28 2023

@author: rc22abq
"""

# 1.1.4 Numpy Arithmetic and Statistical Functions

import numpy as np



# Part 1

arr = np.array([np.pi, np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print(arr)

# Element-wise sin
print("\nnp.sin(arr)", np.sin(arr))

# Element-wise cos
print("\nnp.cos(arr)", np.cos(arr))

# Element-wise tan
print("\nnp.tan(arr)", np.tan(arr))





# Part 2

arr2 = np.arange(1,11,1)
print("\narr2 =", arr2)

# Element-wise exponentials
print("\nnp.exp(arr2)", np.exp(arr2))

# Element-wise logarithms
print("\nnp.log(arr2)", np.log(arr2))