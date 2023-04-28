# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:31:11 2023

@author: jdpev
"""
import pandas as pd

tips = pd.read_csv('tips.csv')
print('\n',tips.head())

party_counts = pd.crosstab(tips['day'], tips['size'])
print('\n', party_counts)

# Note there are not many 1- and 6-person parties
party_counts = party_counts.loc[:, 2:5]

# Normalise so that each row sums to 1
party_pcts = party_counts.div(party_counts.sum(1), axis=0)
print('\n', party_pcts)

# Create the plot
party_pcts.plot.bar()