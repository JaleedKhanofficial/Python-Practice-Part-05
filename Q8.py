# Write a program to create a new dictionary by swapping the keys and values of an existing dictionary.

print("** Reverse Key-Value Pairs **")

# Define the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Create a new dictionary with reversed key-value pairs
reversed_dict = {value: key for key, value in my_dict.items()}

# Print the reversed dictionary
print("Reversed Dictionary:", reversed_dict)

# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial