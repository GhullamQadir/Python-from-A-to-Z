# Creating strings
s1 = 'Hello'
s2 = "World"
s3 = '''Multi
line string'''

# Indexing & Slicing
text = "Python"
print(text[0])      # P
print(text[-1])     # n
print(text[0:3])    # Pyt
print(text[::2])    # Pto (every 2nd char)

# String methods
text = "  python programming  "
print(text.strip())         # "python programming"
print(text.lower())         # "  python programming  "
print(text.upper())         # "  PYTHON PROGRAMMING  "
print(text.replace("python", "Java"))
print(text.split())         # ['python', 'programming']
print("-".join(["a", "b"])) # a-b

# Formatting
name = "Bilal"
age = 30
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
