
words = input("Enter the string: ").split()

def longest_word_in_string(words):
    longest = ""  # Variable to hold the longest word
    for word in words:
        if len(word) > len(longest):  
            longest = word
    return longest


print("The longest word is:", longest_word_in_string(words))
