# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:36:04 2023

@author: User
"""

import requests
import numpy as np

# Define URL.
uk = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmean/date/UK.txt'

lines = uk.readlines()

# Change date format
from datetime import date
thedate = date.fromisoformat(thedate)

# Use requests.
r = requests.get(uk)

# Get the text.
data = r.text

# Split it into lines based on newline character.
lines = data.split('\n')

# List to store maximum month.
max_month = []

# Loop over lines.
for line in lines:
    entries = line.split()
    if entries[0]=='jan':
        max_month.append(entries[0])
    elif entries[0]=='feb':
        max_month.append(entries[0])
    elif entries[0]=='mar':
        max_month.append(entries[0])
    elif entries[0]=='apr':
        max_month.append(entries[0])
    elif entries[0]=='may':
        max_month.append(entries[0])
    elif entries[0]=='jun':
        max_month.append(entries[0])
    elif entries[0]=='jul':
        max_month.append(entries[0])
    elif entries[0]=='aug':
        max_month.append(entries[0])
    elif entries[0]=='sep':
        max_month.append(entries[0])
    elif entries[0]=='oct':
        max_month.append(entries[0])
    elif entries[0]=='nov':
        max_month.append(entries[0])
    elif entries[0]=='dec':
        max_month.append(entries[0])
        
# Turn it into an array.
max_month = np.array(lines)        
     
max_month_value = max(max_month)      

print(max_month_value)


    
    
    
   