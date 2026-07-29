"""
Exercise:
Move the last three items of a list to the beginning while
keeping their original order.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

last_three = numbers[-3:]
remaining_items = numbers[:-3]

result = last_three + remaining_items

print(result)