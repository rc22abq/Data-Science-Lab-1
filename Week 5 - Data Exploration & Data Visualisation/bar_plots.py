# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:14:33 2023

@author: jdpev
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2,1)

data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))

# Set the plots to black and use partial transparency using
# color = 'k' and alpha = 0.7

data.plot.bar(ax=axes[0], color='k', alpha=0.7)
data.plot.barh(ax=axes[1], color='k', alpha=0.7)