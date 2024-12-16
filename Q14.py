# Write a program to find the key with the maximum value and the key with the minimum value in a dictionary.

print("** Find Keys with Maximum and Minimum Values **")

# Define the dictionary
my_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 15}

# Find the keys with the maximum and minimum values
max_key = max(my_dict, key=my_dict.get)
min_key = min(my_dict, key=my_dict.get)

# Print the results
print("Key with the maximum value:", max_key)
print("Key with the minimum value:", min_key)

# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial