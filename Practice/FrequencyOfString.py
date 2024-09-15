def Frequency(String):
    frequency={}
    
    for char in String:
        if char !=' ':  #ignores Spaces
            if char in frequency:
                frequency[char] +=1
            else:
                frequency[char] = 1

    return  frequency

print("Enter a string:")
String=input()


print(Frequency(String))

