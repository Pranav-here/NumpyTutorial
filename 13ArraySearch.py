# To search for a method, we can use where method

import numpy as np

arr = np.array([1,4, 5,6,4, 3,4,5, 3,9,4, 46,4,3,3])
newarr = np.where(arr == 4)
print(newarr)  # Retunrs the indexs as a tuple

# searchsorted performs binary search in an array, assuming the array is sorted

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)


arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')   # Searches from rightside(returns an index form right)
print(x)

# Search for multiple values

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
