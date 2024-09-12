# Defining a class with a constructor
class Car:
    # Constructor to initialize attributes
    def __init__(self, make, model, year):
        self.make = make  # Car manufacturer
        self.model = model  # Car model
        self.year = year  # Manufacturing year
    
    # Method to display car details
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Creating objects using the constructor
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2018)

# Accessing methods
car1.display_info()  # Output: Car: 2020 Toyota Corolla
car2.display_info()  # Output: Car: 2018 Honda Civic
