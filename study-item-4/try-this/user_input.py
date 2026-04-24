"""Practice getting user input and converting data types.

This script demonstrates:
- input() returning strings
- converting input to int and float
- handling type-related errors
"""
name = input("Hvad hedder du?")
print("Hej", name)

print("=" * 40)
print("STRING INPUT".center(40))
print("=" * 40)

# input() returns string by default
age_str = input("Hvor gammel er du?")
print("Age (string):", age_str)
print("Type of age:", type(age_str))

print("=" * 40)
print("INTEGER INPUT".center(40))
print("=" * 40)

# convert input to integer for numeric operations
age_int = int(input("Hvor gammel er du?"))
print("Age (integer):", age_int)
print("Type of age:", type(age_int))

print("=" * 40)
print("FLOAT INPUT".center(40))
print("=" * 40)

# convert input to float to accept decimal values
price = float(input("Enter price: "))
print( "Price:", price)
print("Type of price:", type(price))