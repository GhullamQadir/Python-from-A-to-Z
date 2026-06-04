# Tuples are immutable
coordinates = (10, 20)
person = ("Bilal", 25, "Engineer")

# Unpacking
name, age, job = person

# Single element tuple (needs comma)
single = (5,)       # NOT (5)

# Tuple methods
print(person.count("Bilal"))    # 1
print(person.index(25))         # 1
