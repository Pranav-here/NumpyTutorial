# Splitting is reverse joining
import numpy as np
# We use array_split() for splitting arrays, we pass it the array we want to split
# and the number of splits.

arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr, 3)
print(newarr)  # Returns 3 arrays

newarr = np.array_split(arr, 4)  # This will not work with np.split()
print(newarr)


arr1 = newarr[0]
print(arr1)  # This is how we access it


# splitting 2d arrays

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)  # Returns 3 2d arrays

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)


# We can also mention around what access do we what to split

newarr = np.array_split(arr, 3, axis=1)
print(newarr)

print(newarr[0])


# Alternates like hsplit, vsplit, and d split
