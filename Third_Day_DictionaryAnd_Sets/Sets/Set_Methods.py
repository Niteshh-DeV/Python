"""
set.add(el) #Adds Element
set.remove(el) #Removes the element
set.clear() #Empties the set
set.pop()  #Removes a random Value

set.union(set2) #Combines Both Set VAlues and returns New
set.intersection(set2) #Combines Common values and returns new

"""

Emty_set= set() 
Emty_set.add(3)
Emty_set.add("Nitesh")
Emty_set.add(3)
Emty_set.add(4)
Emty_set.add((1,4,3,6,7))

print(Emty_set)

Emty_set.remove(4)
print(Emty_set)

# Emty_set.clear()
# print(Emty_set)
# print(len(Emty_set))

print(Emty_set.pop())
