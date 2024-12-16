# Write a program to take two lists (keys and values) from the user, create a dictionary, and calculate the total of all values.

print("** Convert Two Lists into a Dictionary and Calculate Total **")

# Input keys and values from the user
keys = input("Enter keys separated by commas: ").split(',')
values = list(map(int, input("Enter values separated by commas: ").split(',')))

# Create a dictionary by zipping the keys and values
my_dict = dict(zip(keys, values))

# Print the dictionary and calculate the sum of values
print("Generated Dictionary:", my_dict)
print("Sum of all values:", sum(my_dict.values()))

# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial