# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 15:51:55 2023

@author: User
"""

import numpy as np

# Create 3x4x4 array
arr = np.linspace(1,48,48).reshape(3,4,4)
print("Original array = \n", arr)

# Indexing 20.0
print("\narr[4,3] =", arr[1,0,3])

# Indexing [9. 10. 11. 12.]
print("\narr[1,2] =", arr[0,2])

# Indexing [[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47. 48.]]
print("\narr[2] = \n", arr[2])

# Indexing [[5. 6.], [21. 22.] [37. 38.]]
print("\narr[0,1,0:2], arr[1,1,0:2], arr[2,1,0:2] =", arr[0,1,0:2], arr[1,1,0:2], arr[2,1,0:2])

# Indexing [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
#arr[:,[0,3,2]] = arr[:,[0,2,3]]
#print("\narr[x,2,0] =", arr)

arr2 = []
for i in range(len(arr)):
    arr2.append(arr[i][::-1])
print("Before changing order:\n")
for rows in arr:
    print(rows)
print("\nAfter changing order:\n")
for rows in arr2:
    print(rows)

# Indexing[[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]


# Indexing[[1. 4.] [45. 48.]]


# Indexing [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]
print("\narr[1,2:3], arr[2,0:2]", arr[1,2:4], arr[2,0:2])