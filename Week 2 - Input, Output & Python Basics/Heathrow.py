# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:37:43 2023

@author: User
"""

import requests
import numpy as np

# Define URL.
heathrow = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt'

# Use requests.
r = requests.get(heathrow)

# Get the text.
data = r.text

# Split it into lines based on newline character.
lines = data.split('\n')

# List to store rainfall.
mm_of_rain = []

# Loop over lines - starting at index 7 since there are 7 header lines to ignore
for line in lines[7:]:
    # Split the line into columns.
    entries = line.split()
    # Column 2 is the month ID - we want August = 8.
    if entries[1]=='8':
        # The 6th column is the rainfall
        # which we cast as a float and append.
        mm_of_rain.append(float(entries[5]))

# Turn it into an array.
mm_of_rain = np.array(mm_of_rain)

# Calculate the mean
average_amount_of_rain = np.mean(mm_of_rain)

# The latest value is at the [-1] index, which we compare to the mean
# Normalised by the standard deviation.
significance = (mm_of_rain[-1]-average_amount_of_rain) / np.std(mm_of_rain)

# Print the information to the screen
print(f'On average we expect {average_amount_of_rain:.1f} mm of rain in August at Heathrow.')
print(f'This August {mm_of_rain[-1]:.1f} mm of rain were recorded, equivalent to {significance:.2f} standard deviations from the mean.')

