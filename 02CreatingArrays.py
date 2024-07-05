# We can create a NumPy ndarray object by using the array() function.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])  # We can pass in a list tuple or any array type object
print(arr)
print(type(arr))

# 0-D arrays

arr0 = np.array(42)
print(arr0)

# 1-D arrays

arr1 = np.array([1,2,3])
print(arr1)

# 2-D arrays: Arrays that have 1D arrays as elements

arr2 = np.array([[1,2],[3,4]])
print(arr2)

# 3-D Arrays: An array that has 2-D arrays (matrices) as its elements

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3)


# We can check the number of dimensions using the ndim function
print(arr3.ndim)

# We can define the number of dimensions while creating an array

arr4 = np.array([1,2,3], ndmin = 5)
print(arr4, arr4.ndim)
