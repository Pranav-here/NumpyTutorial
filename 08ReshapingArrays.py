# By Reshaping we can add or remove or change the number of elements in each dimension
# of an array

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3) # 4 arrays with 3 elements each
print(newarr)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2) # 2 sets of 3 arrays with 2 elements each
# newarr = arr.resphape(2, 3, 4) will raise an error
print(newarr)

print(arr.reshape(3,2,2).base) # Returns the original array, so it's a view



# We are allowed to have one unknown dimension, using -1

newarr = arr.reshape(-1,6)
print(newarr) # 2 arrays with 6 elements each


# To flatten a multi dimensional array to a 1D array

# reshape(-1)

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
