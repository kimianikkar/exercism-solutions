"""
Exercise: Sort a list of lists by the second element.

Goal:
Write a key function that returns the second element of each
inner list and use it with sort() to sort the list.
"""

# Sample data
data = [
    [1, 2, 3],
    [2, 1, 3],
    [4, 0, 1]
]

# Helper function
def find_second_element(item):
    return item[1]

# Sort and display the result
data.sort(key=find_second_element)
print("Sorted list of lists based on the second element:", data )