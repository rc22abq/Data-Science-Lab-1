# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 16:29:05 2022

@author: jdpev
"""
# In this code, we calculate the months with highest temperatures only
# It is left as an exercise to also include lowest temperatures


import requests

# Later, we have numbers instead of calendar months. This is used to fix that
import calendar
# Later, we will print the most common month with highest temperature
import statistics as stat

# Define URL.
data = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmean/date/UK.txt'

# Use requests.
r = requests.get(data)

# Get the text.
data2 = r.text

# Split it into lines based on newline character.
lines = data2.split('\n')

# Lists to store months with highest temperatures, and the temperature itself
max_temp_month = []
max_temp_temp = []

# Loop over lines - starting at index 6
# since there are 6 header lines to ignore
for line in lines[6:-1]:        # -1 as latest year does not include December
    # Split it into a list where the separator is any whitespace
    line_new = line.split()
    # Our list will be full of strings. We need to convert these into floats.
    line_new_float = [float(i) for i in line_new[1:13]]
    # Find the max temperature
    max_temp = max(line_new_float)
    # Find the month in which the max temperature is achieved
    index_max = line_new_float.index(max_temp)
    # Change number into month, accounting for the indexing
    month_max = calendar.month_name[index_max+1]
    # Add this month to the list of months with highest temperatures
    max_temp_month.append(month_max)
    max_temp_temp.append(max_temp)
    
# Now let's summarise what we have found    
print('The months with the highest temperature are given as follows:\n\n',
      max_temp_month)
print('\nand the maximum temperatures respectively are:\n\n',max_temp_temp)
print('\nThe most common month with highest temperature is',
      stat.mode(max_temp_month))
print('The average temperature in',stat.mode(max_temp_month),
      'was',stat.mean(max_temp_temp),'degrees')

# Finally, we print out the hottest month/year ever
hottest_temp = max(max_temp_temp)
hottest_month = max_temp_month[max_temp_temp.index(hottest_temp)]
hottest_year = 1884+max_temp_temp.index(hottest_temp)
print('\nThe hottest temperature recorded was',hottest_temp,
      'and it was in',hottest_month, hottest_year)



# For part 2, we need to provide a given temperature for a 
# given month and year
# For a little extra, we ask the user for the given time periods.
# As an extra exercise, you could provide a rolling average of temperatures
# For this month and over the given time period

# Ask for the month
prompt1 = '\nChoose a month of the year. Please give this as a number'
prompt1 += ' (For instance, instead of January, input 1): '

question1 = input(prompt1)

# Ask for the year
prompt2 = '\nGreat, now choose a year between 1884 and 2021: '
question2 = input(prompt2)
chosen_year = int(question2)-1884

# Check we are happy with the choices
prompt_3 = "Are you happy with your choices? (Yes or No): "
decision = input(prompt_3)

# React to final question and output results
if decision.lower() == 'yes':
	print('Good. In that case, the temperature for this year and month was',
       lines[6+chosen_year].split()[int(question1)])    
elif decision.lower() == 'no':
    print('Too bad. I am taking your first answers only. The temperature for',
          'this year and month was',
          lines[6+chosen_year].split()[int(question1)])