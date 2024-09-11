

# 'r+' mode: Opens a file for both reading and writing. The file must exist, or it will raise an error.
file = open("example_r_plus.txt", "w")  # First, creating a file to use with 'r+' mode
file.write("Initial content for 'r+' mode.\n")
file.close()

file = open("example_r_plus.txt", "r+")  # Opening the file with 'r+' mode
print("\nContent of file before writing in 'r+' mode:")
print(file.read())  # Reading the initial content

file.seek(0)  # Moving the file pointer to the start for writing
file.write("Updated content using 'r+' mode.\n")  # Writing will overwrite from the start
file.seek(0)  # Moving the file pointer to the start for reading
print("\nContent after writing with 'r+':")
print(file.read())  # Reading the updated content
file.close()
