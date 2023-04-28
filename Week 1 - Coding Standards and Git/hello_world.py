# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as mp
import pandas as pd

import matplotlib

print("Hello, World!")

# Using variables.
a = "Hello world."
print(a)

b = 5*2
c = (10/2)+2

print(b)
print(c)
print(b+c)
print(b*c)


# Concatenating.
msg1 = "Hello"
msg2 = "john"
x = msg1 + msg2
print(x)
print(f'{msg1},_{msg2}')


# Asking for inputs.
num1 = int(input("Enter a number."))
num2 = int(input("Enter a different number."))
num3 = num1 + num2
print("\nThe addition of the two numbers you entered is {}.".format(num3))