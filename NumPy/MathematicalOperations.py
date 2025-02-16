import numpy as np

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

print (list1 + list2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] means concatenation of two lists.

array1 = np.array(list1)
array2 = np.array(list2)

print ("Sum")
print (array1 + array2)# [ 7  9 11 13 15] means element wise addition of two arrays.
 # print(np.add(array1, array2)) 

print ("Difference")
print (array1 - array2)# [-5 -5 -5 -5 -5] means element wise subtraction of two arrays.
    # print(np.subtract(array1, array2))
    
print ("Product")
print (array1 * array2) # [ 6 14 24 36 50] means element wise multiplication of two arrays.
    # print(np.multiply(array1, array2))

print ("Division")    
print (array1 / array2) # [0.16666667 0.28571429 0.375      0.44444444 0.5       ] means element wise division of two arrays.
    # print(np.divide(array1, array2))


print (array1 + 5) # [6 7 8 9 10] means adding 5 to each element of the array.
print (array1 - 5) # [-4 -3 -2 -1  0] means subtracting 5 from each element of the array.
print (array1 * 5) # [ 5 10 15 20 25] means multiplying 5 to each element of the array.
print (array1 / 5) # [0.2 0.4 0.6 0.8 1. ] means dividing each element of the array by 5.


array3 = np.array([[1,2,3],[4,5,6]])
print(array3)
print (array3.shape)
print ("Transpose")
transpose = np.transpose(array3) # [[1 4]  
                                #  [2 5]
                                #  [3 6]] means transpose of the array. \\
print (transpose)
print (transpose.shape)

# arrey.T is also used to find the transpose of the array. 
# print(array3.T) # [[1 4]
                 #  [2 5]
                 #  [3 6]] means transpose of the array.
                 

print ("Reshape")
array4 = np.random.randint(10,50,(2,3)) # 3x3 array with random numbers between 10 and 50
print(array4)
print(array4.shape)
array5 = array4.reshape(3,2) # 3x2 array
print(array5)
print(array5.shape)