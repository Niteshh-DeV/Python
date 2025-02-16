import numpy as np

# 2D array
b = np.array([[1, 2, 3], [4, 5, 6]]) #b = np.array([(1, 2, 3), (4, 5, 6)]) is also valid

print(b)

print(b.shape)  # (2, 3) means 2D array with 2 rows and 3 columns. It gives the shape of the array. Rows, columns, etc.
print(b[0, 0])  # 1
print(b[0, 1])  # 2
print(b[0, 2])  # 3
print(b[1, 0])  # 4
print(b[1, 1])  # 5
print(b[1, 2])  # 6
print(b[0])     # [1 2 3]
print(b[1])     # [4 5 6]


c = np.array([(1,2,3),(3,4,5)],dtype = float) #dtype is optional. It is the data type of the array elements. It is int by default.
print(c)