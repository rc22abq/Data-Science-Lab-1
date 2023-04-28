# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:05:09 2023

@author: User
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pres = pd.read_csv('president_heights.csv')
print(pres)

plt.figure()
plt.hist(pres['height(cm)'])
plt.show()

print("\n25th percentile =", np.percentile(pres['height(cm)'], 25))
print("\n50th percentile =", np.percentile(pres['height(cm)'], 50))
print("\n75th percentile =", np.percentile(pres['height(cm)'], 75))

plt.figure()
plt.plot(pres['height(cm)'])
plt.show()