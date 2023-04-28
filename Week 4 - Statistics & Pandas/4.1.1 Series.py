# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:18:24 2023

@author: User
"""

# 4.1.1 Series

from pandas import Series

s = Series([9000000,1150000,612000,579000,572000],
           index = ['London','Birmingham','Glasgow','Liverpool','Bristol'])

print('s =\n', s, '\n')

print(s[1:2])
