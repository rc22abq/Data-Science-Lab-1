# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 12:27:17 2023

@author: User
"""

import requests
import numpy as np

# Define URL.
uk = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmean/date/UK.txt'

# Use the open() built-in function
myfile = open('UK.txt','r')

lines = myfile.readlines()
year, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec, win, spr, sum, aut, ann = lines[5].split()
print(year, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec, win, spr, sum, aut, ann)

from datetime import datetime
jan = datetime.strptime(jan, '%B').month