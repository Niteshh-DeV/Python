import numpy as np

array = np.random.randint(10,50,(3,3)) # 3x3 array with random numbers between 10 and 50
print(array)

print(array.shape ) # (3, 3) means 2D array with 3 rows and 3 columns.

print (array.ndim) # 2 means 2D array. It gives the number of dimensions of the array.

print (array.size) # 9 means 9 elements in the array. It gives the number of elements in the array.

print (array.dtype) # int64 means the data type of the array elements. It gives the data type of the array elements.