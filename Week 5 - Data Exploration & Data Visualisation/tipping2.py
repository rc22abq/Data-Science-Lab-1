# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:59:24 2023

@author: jdpev
"""

import pandas as pd
import seaborn as sns

tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])

print(tips.head())

# seaborn takes a data argument which can be a DataFrame. The other arguments
# are then referring to column names. Because there are multiple observations
# for each value in the day, the bars are the average value of tip_pct.
sns.barplot(x='tip_pct', y='day', data=tips, orient='h')

# Suppose we also wanted to include a time element. We can use the hue option.
# Simply add hue='time' to the above.
# sns.barplot(x='tip_pct', y='day', hue = 'time', data=tips, orient='h')
# Notice that seaborn automatically changes
# the aesthetics of plots. We can switch between different plot appearances
# using seaborn.set