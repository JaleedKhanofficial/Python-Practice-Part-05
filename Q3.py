# Write a program that asks the user for a key and prints the corresponding value if the key exists in the dictionary. If the key doesn’t exist, print "Key not found."

print("** Find the Value for a Key **")

# Define the dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Ask the user for a key
key = input("Enter a key: ")

# Check if the key exists and print the corresponding value
if key in my_dict:
    print(f"The value for '{key}' is:", my_dict[key])
else:
    print("Key not found.")

# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial