import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0
    
    while True:
        guess = input("Guess a number between 1 and 100: ")
        
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
