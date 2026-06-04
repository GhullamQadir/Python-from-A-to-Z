# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Accessing
print(fruits[0])        # apple
print(fruits[-1])       # cherry

# Slicing
print(fruits[1:3])      # ['banana', 'cherry']

# Modifying
fruits.append("orange")
fruits.insert(1, "mango")
fruits.remove("banana")
popped = fruits.pop()   # removes last
fruits.sort()
fruits.reverse()

# List comprehension
squares = [x**2 for x in range(5)]          # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]

# Copying
new_fruits = fruits.copy()      # or list(fruits) or fruits[:]
