import numpy as np

np_array = np.array([1, 2, 3, 4, 5])
print(np_array)
print(type(np_array))   # ndarray is the data type of the array in numpy. Its N dimensional array.

print ("Zeros matrix")
zero = np.zeros((2, 3))  # 2 rows and 3 columns with all zeros. It is a 2D array.
print(zero)

print ("Ones matrix")
one  = np.ones((3, 3))   # 3 rows and 3 columns with all ones. It is a 2D array.
print(one)

print ("Full matrix")
full = np.full((5, 4), 7)  # 5 rows and 4 columns with all 7s. It is a 2D array.
print(full)

print ("Identity matrix")
Iddenity = np.eye(3)  # 3x3 matrix with 1s on the diagonal and 0s elsewhere. It is a 2D array.
print(Iddenity)

print ("Random 3x2 matrix with random values")
random = np.random.random((3, 2))  # 3x2 matrix with random values. It is a 2D array.
print(random)

print ("Random 3x3 matrix with random values between 1 and 10")
random = np.random.randint (1, 10, (3, 3))  # 3x3 matrix with random values between 1 and 10. It is a 2D array.
print (random)

print ("Evenly spaced values between 0 and 30 with step 2")
evenly = np.arange(0, 30, 2)  # 0 to 30 with step 2. It is a 1D array.
print(evenly)

print ("Evenly spaced 5 values between 0 and 30")
evenly = np.linspace(20, 30, 5)  # 0 to 30 with 5 values. It is a 1D array.
print(evenly)