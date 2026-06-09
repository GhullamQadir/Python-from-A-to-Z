# Defining functions
def greet(name):
    """This is a docstring (function documentation)"""
    return f"Hello, {name}!"

print(greet("Amjad"))

# Default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(3))         # 9 (3²)
print(power(2, 3))      # 8 (2³)

# Keyword arguments
def person_info(name, age, city):
    return f"{name}, {age}, {city}"

print(person_info(age=30, city="Nawabshah", name="Tanveer"))

# Arbitrary arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))      # 10

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Amjad", age=25)

# Scope
global_var = 10

def test():
    local_var = 5
    print(global_var)   # Can read global
    # To modify global:
    global global_var
    global_var = 20

# Lambda functions
square = lambda x: x ** 2
print(square(5))        # 25

# Higher-order functions
def apply_operation(num, operation):
    return operation(num)

print(apply_operation(5, lambda x: x * 2))  # 10
