# Creating sets (unordered, no duplicates)
numbers = {1, 2, 3, 4, 5}
empty_set = set()       # NOT {} (that's dict)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)            # Union: {1, 2, 3, 4, 5}
print(a & b)            # Intersection: {3}
print(a - b)            # Difference: {1, 2}
print(a ^ b)            # Symmetric difference: {1, 2, 4, 5}

# Methods
numbers.add(6)
numbers.remove(3)       # KeyError if missing
numbers.discard(10)     # No error if missing
