# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    value = int("abc")
except (ValueError, TypeError):
    print("Invalid conversion")

# Else and Finally
try:
    num = int("10")
except ValueError:
    print("Error")
else:
    print(f"Success: {num}")    # Runs if no exception
finally:
    print("Always runs")        # Cleanup code

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

# Custom exceptions
class ValidationError(Exception):
    pass

def check_username(username):
    if len(username) < 3:
        raise ValidationError("Username too short")
