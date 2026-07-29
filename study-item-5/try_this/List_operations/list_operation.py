"""
Exercise: Safwly remove an Item from a List

Goal:
Remove an item only if it exists in the list.
Then modify the code to remove the item only if it appears more than once.
"""

# Example 1: Remove an item only if it exists 
x = [1, 2, 3, 4, 5]
item = 3

if item in x:
    x.remove(item)
print("Updated List x:", x)

# Example 2: Remove an item only if it appears more than once
y = [1, 2, 3, 4, 5, 3]
item_to_remove = 3

if y.count(item_to_remove) > 1:
    y.remove(item_to_remove)

print("Updated List y:", y)   