from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Map
squares = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# Reduce
product = reduce(lambda x, y: x * y, numbers)
# 120

# Combined
result = list(map(lambda x: x**2, filter(lambda x: x > 2, numbers)))
# [9, 16, 25]
