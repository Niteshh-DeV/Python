
# 'a+' mode: Opens a file for both reading and appending. If the file doesn't exist, it creates the file.
file = open("example_a_plus.txt", "a+")  # Open the file in 'a+' mode (creates it if not present)
file.write("Appended line using 'a+' mode.\n")  # Writing (this will be appended at the end)
file.seek(0)  # Moving the file pointer to the start for reading
print("\nContent of file after writing with 'a+':")
print(file.read())  # Reading the entire content including the appended line
file.close()

