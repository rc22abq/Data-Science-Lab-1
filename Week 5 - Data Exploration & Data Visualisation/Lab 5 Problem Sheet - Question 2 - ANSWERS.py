# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:56:52 2023

@author: User
"""

import numpy as np
from scipy import stats

dam_height = [756, 726, 710, 568, 564, 440, 440]

print("Mean =", np.mean(dam_height))
print("Median =", np.median(dam_height))
print("Mode =", stats.mode(dam_height))
print("STD =", np.std(dam_height))
print("Variance =", np.std(dam_height) ** 2)
print("IQR =", np.percentile(dam_height, 75) - np.percentile(dam_height, 25))