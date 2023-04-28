# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 14:05:17 2023

@author: User
"""

guests = ['Riya','Dave','Sam','Hope','Connie','Anna']

n = len(guests)
guests.sort()

print("Number of guests invited =",n)

guests.append('Jake')
guests.append('Harry')
guests.remove('Connie')
m = len(guests)
guests.sort()

print("The updated number of guests invited =",m)

print("Dear", guests[0],
      "you are invited for dinner this Friday at Pizza Express.")
print("Dear", guests[1],
      "you are invited for dinner this Friday at Pizza Express.")
print("Dear", guests[2],
      "you are invited for dinner this Friday at Pizza Express.")
print("Dear", guests[3],
      "you are invited for dinner this Friday at Pizza Express.")
print("Dear", guests[4],
      "you are invited for dinner this Friday at Pizza Express.")
print("Dear", guests[5],
      "you are invited for dinner this Friday at Pizza Express.")
print("Dear", guests[6],
      "you are invited for dinner this Friday at Pizza Express.")