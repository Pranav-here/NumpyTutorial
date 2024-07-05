import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

print(arr+5)
print(arr*5)

a = np.array([1,2,3,4])
b = np.array([1,2,3,4])

add_result = a + b
print("Addition:", add_result)
sub_result = a - b
print("Subtraction:", sub_result)
mul_result = a * b
print("Multiplication:", mul_result)
div_result = a / b
print("Division:", div_result)


# Central modes of tendency

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Max:", np.max(data))
print("Min:", np.min(data))
print("Standard Deviation:", np.std(data))


# Transpose of an array

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
transposed_array = array_2d.T
print("Transposed array:\n", transposed_array)


# Logical operators


a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

# Element-wise comparison
print("a > b:", a > b)
print("a == b:", a == b)

# Logical operations
print("Logical AND:", np.logical_and(a > 2, b < 4))
print("Logical OR:", np.logical_or(a < 3, b > 1))






# Adding arrays with different dimensions
# We cannot add arrays with different array shapes

arr1 = np.array([1,2])
arr2 = np.array([[1,2],[3,4]])

print(arr1+arr2)
