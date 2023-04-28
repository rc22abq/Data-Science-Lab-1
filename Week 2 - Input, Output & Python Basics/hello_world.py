# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 12:50:48 2023

@author: User
"""

print('Hello, world!')

message = 'Hello, world!'
print(message)

a, b = 1, 2.0    # This is how we can declare multiple variables on the same line
# If we are unsure of an object's data type, we can simply enquire.
print(type(a))
print(type(b))
print(type(message))
# We can change a data type
a = float(a)
print(type(a))

print('Hello, \tWorld!')
print('Hello \nWorld!')

print('Hello, World!          '.rstrip())
print('Hello, World!          '.lstrip())
print('Hello, World!          '.strip())