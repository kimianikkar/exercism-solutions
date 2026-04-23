def convert(number):
    """
    Convert a number into a raindrop string.

    If the number is divisible by:
    - 3, add "Pling"
    - 5, add "Plang"
    - 7, add "Plong"

    If none of these apply, return the number as a string."""
    
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if not result:
        result = str(number)
    return result