import numpy as np

# 3D array
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(c)

print(c.shape)  # (2, 2, 3) means 3D array with 2 rows, 2 columns and 3 depth.

print(c[0, 0, 0])  # 1
print(c[0, 0, 1])  # 2
print(c[0, 0, 2])  # 3
print(c[0, 1, 0])  # 4
print(c[0, 1, 1])  # 5
print(c[0, 1, 2])  # 6
print(c[0, 0])     # [1 2 3]
print(c[0, 1])     # [4 5 6]
print(c[1, 0, 0])  # 7
print(c[1, 0, 1])  # 8
print(c[1, 0, 2])  # 9
print(c[1, 1, 0])  # 10
print(c[1, 1, 1])  # 11
print(c[1, 1, 2])  # 12
print(c[1, 0])     # [7 8 9]
print(c[1, 1])     # [10 11 12]
print(c[0])        # [[1 2 3]
                   #  [4 5 6]]
print(c[1])        # [[7 8 9]
                     #  [10 11 12]] 
