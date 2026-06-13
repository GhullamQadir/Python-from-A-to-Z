# Importing modules
import math
print(math.sqrt(16))        # 4.0

from math import pi, pow
print(pi)

# Import with alias
import datetime as dt
now = dt.datetime.now()

# Built-in modules
import random
print(random.randint(1, 10))
print(random.choice(["apple", "banana"]))

import os
print(os.getcwd())          # Current directory

# Creating your own module
# Save as mymodule.py:
"""
def greet(name):
    return f"Hello, {name}!"
"""

# Then import:
# import mymodule
# print(mymodule.greet("Peterson"))
