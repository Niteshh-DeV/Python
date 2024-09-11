
# This is a simple Program to open a file in Write mode

file = open("First.txt","w")
file.write ("This  is the first line of the file \n")
file.write("This  is the second line of the file\n")

file.close() #Close the file

#Open File in Read mode

file = open ("First.txt","r")

content=file.read()

print(content) #This reads The content in a file.

file.close() #Close the file

#Open File In append mode to add data into existing  file


file = open("First.txt","a")
file.write("This is appended Line of code")

file.close()

#Now Open the file in  Read mode to see the appended line of code
file = open("First.txt","r")
for line in  file:
    print(line,end='') #This reads The content in a file.

