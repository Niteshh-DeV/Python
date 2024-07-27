Info={
    "Key" : "Value",
    "Name" :"Nitesh" ,
    "Learning" : "Coding" ,
    "Age" : 18 ,
    "Marks" : 34.2 ,
    "Is_adult" : True
}

# print(Info.keys()) # Returns All keys

# print(list(Info.keys())) #Typecasted to Lists

# print(len(Info))

# print(len(list(Info.keys())))

# print(Info.values()) #Returns All The Values

# print(Info.items()) # returns All (Key , Value) pairs as touple

# pairs=list(Info.items())
# print(pairs[3])
# print(type(pairs))

print(Info.get("Age")) #Returns The Key According to Value

print(Info.update({"City":"Mahendranagar"})) #inserts teh Specified items to the Dictionary
print(Info)
