# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:31:35 2023

@author: User
"""

import pandas as pd
import numpy as np

cities_dict = {'London':9000000, 'Birmingham':1150000, 'Glasgow':612000,
               'Liverpool':579000, 'Bristol':572000}

cities = pd.Series(cities_dict)
print(cities['London'])

print(cities.iloc[1]) # prints the second value

print(np.sort(cities)[-2]) # sorts the cities series smallest to largest and prints the second largest value
# Negative numbers start counting from the last element