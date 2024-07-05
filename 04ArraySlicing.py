# We pass slice instead of index like this: [start:end].

# We can also define the step, like this: [start:end:step].(default [0:len(arr):1])
# The result includes the start index, but excludes the end index.
import numpy as np

arr1 = np.array([1,2,3,4,5,6,7])
print(arr1[1:4])
print(arr1[4:])
print(arr1[:4])
print(arr1[-3:-1])
print(arr1[2:6:2])
print(arr1[::2])

# arr[start_row:end_row, start_col:end_col]

arr2 = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(arr2[1, 1:4])
print(arr2[0:2, 2])
