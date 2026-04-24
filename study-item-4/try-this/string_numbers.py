"""Practice working with strings, numbers, and math/cmath modules.

This script explores:
- Operations between different data types
- Behavior of strings with numeric types
- Differences between math and cmath modules
"""
print("=" * 40)
print("STRINGS TEST".center(40))
print("=" * 40)

# Strings can be multiplied by integers but not floats or complex numbers
text = "Hello" 
num_int = 5
num_float = 2.5
num_complex = 2 + 3j

print("text * num_int =", text * num_int)
#This operations cause errors:
# print(text * num_float)
# print(text * num_complex)

print("=" * 40)
print("NUMBER TESTS".center(40))
print("=" * 40)

print("num_int + num_float =", num_int + num_float)
# print(num_int + num_complex)

print("num_float * num_complex =", num_float * num_complex)
print("num_int * num_complex =", num_int * num_complex)

print("=" * 40)
print("MATH MODULES".center(40))
print("=" * 40)

# math module works with real numbers
import math
print("math.sqrt =", math.sqrt(16))
print("math.sin =", math.sin(0))

print("=" * 40)
print("CMATH MODULES".center(40))
print("=" * 40)

# cmath module works with complex numbers
import cmath
print("cmath.sqrt(-1) =", cmath.sqrt(-1))
print("cmath.sqrt(16) =", cmath.sqrt(16))