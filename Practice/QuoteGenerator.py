import random

# List of quotes
quotes = [
    "Believe you can and you're halfway there.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Dream big and dare to fail.",
    "Do what you can, with what you have, where you are.",
    "The future belongs to those who believe in the beauty of their dreams."
]

def generate_quote():
    quote = random.choice(quotes)
    print("\n Your Random Quote ✨")
    print(f'"{quote}"\n')

def main():
    print("Welcome to the Random Quote Generator")
    while True:
        user_input = input("Press Enter to get a new quote (or type 'q' to quit): ")
        if user_input == 'q':
            break
        generate_quote()

if __name__ == "__main__":
    main()