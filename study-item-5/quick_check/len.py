"""Quick Check: Understanding len() with nested lists."""

x1 = [0]
x2 = []
x3 = [[1, 3, [4, 5], 6], 7]

print(f"Length of x1: {len(x1)}")  # 1
print(f"Length of x2: {len(x2)}")  # 0
print(f"Length of x3: {len(x3)}")  # 2

# len() only counts elements in the outer list.
