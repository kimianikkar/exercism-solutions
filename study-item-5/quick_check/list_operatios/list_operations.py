"""
Review Question

Question:
What would be the result of len([[1, 2]] * 3)?

Answer:
The result is 3 because the list contains three inner lists.
"""

nested_list = [[1, 2]] * 3

print(len(nested_list)) # Output: 3 





"""
Review Question

Question:
Which expression raises an exception?

Answer:
max([1, 2, "three"]) raises a TypeError because python cannot compare integers and strings.
"""

print(min(["a" , "b", "c"])) # Output: a

# Print(max([1, 2, "three"])) # Raises TypeError 

print([1, 2, 3].count("one")) # Output: 0 
