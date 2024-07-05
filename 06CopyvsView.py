# Copy: Makes a copy of the array, owns the data and changes made will not affect each other
# View: views the original array, does not own the data and changes made affect each other

import numpy as np

arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

y = arr.view()
arr[0] = 34
y[1] = 24
print(arr)
print(y)


# To check if array owns the data or not
# .base: returns none if owned otherwise it refers to the original object

print(x.base)
print(y.base)
print(arr.base)


