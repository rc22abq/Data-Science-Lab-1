# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 16:27:03 2023

@author: User
"""

# First two terms.
n_1, n_2 = 0, 1
count = 0

print("Fibonacci sequence for the first 20 terms:")
while count < 20:
    print(n_1)
    nth = n_1 + n_2
    # Update values.
    n_1 = n_2
    n_2 = nth
    count += 1