# Joining array's helps us in putting 2 or more arrays in a single array
import numpy as np
# In SQL we join based on key
# In numpy we join based on axes

# Axis:
# 0 is vertical
# 1 is horizontal
# default is 0

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr3 = np.concatenate((arr1, arr2))  # Send it in as a tuple
print(arr3)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr4 = np.concatenate((arr1, arr2), axis = 1)
print(arr4)


# Joining using stack functions

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)


# Stacking along rows

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))
print(arr)

# Stacking along columns

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))
print(arr)


# Stacking along height/depth

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))
print(arr)
