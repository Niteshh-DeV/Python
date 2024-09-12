#Code for Classes  and Objects in python

class Person:
    # Method to display person's details
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects
person1 = Person()
person1.name = "ABC"
person1.age = 25

person2 = Person()
person2.name = "XYZ"
person2.age = 30

# Accessing attributes and methods
person1.display_info() 
person2.display_info() 
    
