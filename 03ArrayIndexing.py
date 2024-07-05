# Similar to list indexing, starts from 0

import numpy as np

arr1 = np.array([1,2,3,4,5,6])
print(arr1[0])

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2[0,1])  # second element in first row

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3[0, 1, 2])

# negative indexing

arr4 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
#last element from the second dimension
print(arr4[1, -1])
