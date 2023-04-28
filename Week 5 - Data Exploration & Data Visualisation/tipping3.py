# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 14:34:37 2023

@author: jdpev
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fig, axes = plt.subplots(3,1)

tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])

tips['tip_pct'].plot.hist(ax=axes[0], bins=50)
tips['tip_pct'].plot.density(ax=axes[1])

# The distplot method makes histogram and density plots even easier.
# It can plot both a histogram and a continuous density estimate simultaneously
# e.g. consider a bimodal distribution consisting of draws from two different
# standard normal distributions

comp1 = np.random.normal(0, 1, size=200)
comp2 = np.random.normal(10, 2, size=200)
values = pd.Series(np.concatenate([comp1, comp2]))
sns.distplot( values, bins=100, color='k', ax=axes[2])