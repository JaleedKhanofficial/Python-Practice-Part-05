# Write a program that removes a specified key-value pair from a dictionary and prints the updated dictionary.

print("** Remove a Key-Value Pair **")

# Define the dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Ask the user for the key to remove
key_to_remove = input("Enter the key to remove: ")

# Check if the key exists and remove it
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print("Updated Dictionary:", my_dict)
else:
    print("Key not found.")

# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial