import pandas as pd

data = { 'Name':['Tom', 'nick', 'krish', 'jack'],
         'Age':[20, 21, 19, 18],
         'Address': ['Delhi', 'Mumbai', 'Chennai', 'Kolkata']}

print (data)    

df = pd.DataFrame(data) # This is a 2D data structure. It is similar to a table in a database
# The first column is the index and the second column is the data
# The data type is object which is a string by default

print (df) # This will print the data frame