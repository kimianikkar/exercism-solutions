"""
Exercise:
Using what you know about the len() function and list slices,
combine the two to get the second half of a list when you
don't know its size.
"""

# Create a sample list 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Calculate the starting index of the second half of the list
start_index = len(x) // 2

# Print the second half of the list using slicing
print(x[start_index:])