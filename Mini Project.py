# Project 1: To-Do List (Console)
class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add(self, task):
        self.tasks.append({"task": task, "done": False})
    
    def complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
    
    def show(self):
        for i, task in enumerate(self.tasks):
            status = "✓" if task["done"] else " "
            print(f"[{status}] {i}. {task['task']}")

# Project 2: Simple Calculator
def calculator():
    while True:
        print("\n1. Add  2. Subtract  3. Multiply  4. Divide  5. Quit")
        choice = input("Choose: ")
        if choice == "5":
            break
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        
        operations = {
            "1": lambda a, b: a + b,
            "2": lambda a, b: a - b,
            "3": lambda a, b: a * b,
            "4": lambda a, b: a / b if b != 0 else "Error"
        }
        print("Result:", operations.get(choice, lambda a, b: "Invalid")(num1, num2))

# Project 3: Password Generator
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

# Project 4: Word Counter
def count_words(filename):
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        return len(words), len(set(words))

# Project 5: Number Guessing Game
import random

def guessing_game():
    secret = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess (1-100): "))
        attempts += 1
        if guess == secret:
            print(f"Correct! Took {attempts} attempts.")
            break
        print("Higher!" if guess < secret else "Lower!")
