def isprime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def PrimeChecker():
    print("Welcome to the Prime Number Checker!")
    print("Enter a number, and I'll tell you if it's prime.")
    print("Type 'exit' to quit the program.")
    
    while True:
        user_input = input("\nEnter a number: ")
        
        if user_input.lower() == 'exit':
            print("Thank you for using the Prime Number Checker. Goodbye!")
            break
        
        try:
            number = int(user_input)
            if isprime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    PrimeChecker()