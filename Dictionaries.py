# Creating dictionaries
student = {
    "name": "Johnathan",
    "age": 22,
    "grade": "A"
}

# Accessing
print(student["name"])
print(student.get("age"))
print(student.get("city", "Unknown"))   # default value

# Adding/Updating
student["city"] = "New York"
student.update({"phone": "123-456-7890"})

# Removing
del student["age"]
popped = student.pop("grade")

# Iterating
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
