# Use for loops

import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
for i in arr1:
    print(i)


arr2 = np.array([[1,2,3,4],[5,6,7,8]])
for i in arr2:
    print(i)


for x in arr2:
  for y in x:
    print(y)


arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for i in arr3:
    print(i)


print(arr3.shape)

for x in arr3:
  for y in x:
    for z in y:
      print(z)


# we also use nditer() as an helping function

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):  # for n dimension, instead of using n for loops we can do this
  print(x)




# We can use op_dtypes argument and pass it the expected datatype to change the
# datatype of elements while iterating.

# NumPy does not change the data type of the element in-place
# (where the element is in array) so it needs some other space to perform
# this action, that extra space is called buffer, and in order to enable it in
# nditer() we pass flags=['buffered'].

arr = np.array([1,2,3,4,5])

for x in np.nditer(arr, flags=["buffered"], op_dtypes="S"):
    print(x)

# Iterating with different step size

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):  # Skipping every other scalar element
  print(x)


# Enumerating

arr = np.array([1, 2, 3])  # Same way for 2 d elements
for idx, x in np.ndenumerate(arr):
  print(idx, x)
