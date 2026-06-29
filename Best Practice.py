"""
PEP 8 Style Guide Summary:

1. Naming:
   - Variables/functions: lowercase_with_underscores
   - Classes: CapitalizedWords
   - Constants: UPPERCASE_WITH_UNDERSCORES
   - Private: _leading_underscore

2. Indentation: 4 spaces (no tabs)

3. Line length: Max 79 characters

4. Imports: One per line, grouped (standard, third-party, local)

5. Whitespace:
   - No spaces around = in keyword arguments
   - One space after comma
   - Two blank lines between functions/classes
"""

# Example of clean code
class BankAccount:
    """A simple bank account class."""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        """Add money to account."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        """Remove money from account."""
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self._balance
    
    @property
    def balance(self):
        """Get current balance."""
        return self._balance


# Docstring format
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    
    Returns:
        float: The calculated area.
    
    Raises:
        ValueError: If length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Dimensions must be positive")
    return length * width
