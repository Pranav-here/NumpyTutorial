# The Shape of an Array is the number of elements in each dimension
import numpy as np

# To get the shape of an array

arr = np.array([[1,2,3,4], [5,6,7,8]])
print(arr.shape)
# Returns 2 and 4, which mean that the first dimension has 2 elements and second dimension has 3
# like 2 rows with 4 elements each

arr1 = np.array([1,2,3,4], ndmin = 5)
print(arr1.shape)  # The output here says that 4 elements in innermost(5th) dimension has
# 4 elements, the 4th dimension has 1 element that is the vector
# the 3rd dimension has 1 element that is the matrix with the vector
# the 2nd dimension has 1 element that is the 3D array
# the 1st dimension has 1 element that is the 4D array

# Integers at every index tells about the number of elements the corresponding dimension has.
