# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:39:39 2023

@author: User
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


tips = pd.read_csv('tips.csv')
print(tips)

party_counts = pd.crosstab(tips['day'], tips['size'])
print(party_counts)
party_norm = party_counts.div(party_counts.sum(1),axis = 0)

party_norm.plot.bar()

plt.figure()
plt.hist(tips['tip']/tips['total_bill'])
plt.show()