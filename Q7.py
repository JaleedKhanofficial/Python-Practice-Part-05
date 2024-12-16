# Write a program that takes a string as input and builds a dictionary where the keys are characters and the values are their counts in the string.

print("** Count Occurrences of Characters **")

# Get a string from the user
text = input("Enter a string: ")

# Create an empty dictionary to count occurrences
char_count = {}

# Count each character in the string
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

# Print the character counts
print("Character Counts:", char_count)

# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial