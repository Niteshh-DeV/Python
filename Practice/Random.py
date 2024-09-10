# import random

# A = random.randint(1 , 100)  # random integer number between 1 and 100


# print ("The Random No between  1 to 100 is: ", A)


import random 
B = round(random.random(),1)
print (B)  # This will print a random float number between 0.0 and 1.

import random

B = random.random() * 100  # scales the random float to a value between 0 and 100
print("{:.2f}".format(B))