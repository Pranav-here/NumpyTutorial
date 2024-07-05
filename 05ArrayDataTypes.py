# By default in python we have these data types, strings, boolean, float, integer and complex

# In Numpy we have some extra and refer to them with a single charecter

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

# to check for a datatype, we use .dtype


import numpy as np

arr = np.array([1,2,3,4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

# We can define datatypes during the asisgnment

arr = np.array([1,2,3,4], dtype='S')
print(arr.dtype)

# for i, u, f, S and U we can define the sizes aswell

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

# We will get a value error if the value cannot be casted


# The best way to change the datatype is to make a copy with the astype() and specify
# the new type

arr = np.array([1.1,1.2,1.3])

newarr = arr.astype("i") # or (int)

print(newarr)
print(newarr.dtype)

newarr1 = newarr.astype(bool)
print(newarr1)
