# 'w+' mode: Opens a file for reading and writing. If the file doesn't exist, it creates the file.
# It will overwrite the existing content if the file already exists.
file = open("example_w_plus.txt", "w+")
file.write("This is written using 'w+' mode.\n")  # Writing to the file
file.seek(0)  # Moving the file pointer to the start of the file to read from the beginning
print("Content after writing with 'w+':")
print(file.read())  # Reading the content just written
file.close()  # Closing the file
