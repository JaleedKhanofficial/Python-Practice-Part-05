# Write a program that takes two lists of the same length (one for keys and one for values) and creates a dictionary using these lists.

print("** Dictionary from Two Lists **")

# Define two lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

# Create a dictionary from the two lists
combined_dict = dict(zip(keys, values))

# Print the combined dictionary
print("Combined Dictionary:", combined_dict)

# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial