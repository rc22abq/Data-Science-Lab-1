# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 13:06:43 2023

@author: User
"""

discworld = ['death', 'rincewind', 'the luggage', 'the librarian', 
             'granny weatherwax', 'sam vimes']

print("Hello,", discworld[0].title(),",", discworld[1].title(),",",
      discworld[2].title(),",", discworld[3].title(),",", 
      discworld[4].title(), "and", discworld[5].title(),".")

del discworld[1]
print(discworld)

discworld.pop()
print(discworld)

discworld.remove('death')
print(discworld)