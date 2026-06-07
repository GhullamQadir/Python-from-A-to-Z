age = 18

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")       # This runs
else:
    print("Adult")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"

# Multiple conditions
x = 15
if 10 < x < 20:             # Chained comparison
    print("Between 10 and 20")

# Truthy/Falsy
name = ""
if not name:
    print("Name is empty")
