# In NumPy, you filter an array using a boolean index list.
import numpy as np

# Hardcoding

arr = np.array([1, 2, 3, 4])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)



# Let's try to make a filter array that pnly return values greater than 42

arr = np.array([41, 42, 43, 44])

filter_array = []

for i in arr:
    if i >42:
        filter_array.append(True)
    else:
        filter_array.append(False)

newarr = arr[filter_array]
print(filter_array)
print(newarr)

# Or we can just do

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
