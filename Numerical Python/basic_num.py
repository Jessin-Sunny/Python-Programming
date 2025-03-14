import numpy as np
a = np.array([(1, 2, 3, 4), (7, 8, 9, 10)])  #declare as ndarray
print(a)
print("Array Dimension : ", a.ndim)
print("Array Shape : ", a.shape)
print("Array Size : ", a.size)
print("Array element type : ", a.dtype)
print("Array Item Size : ", a.itemsize)

#slicing
b = np.arange(10)
print(b)
print(b[0])
#change in source array while slicing
var_array = b[0:4]
var_array[:] = 100
print(b)

