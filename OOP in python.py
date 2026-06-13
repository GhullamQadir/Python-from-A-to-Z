# Class and Object
class Dog:
    # Class attribute
    species = "German Shepherd"
    
    # Constructor
    def __init__(self, name, age):
        self.name = name        
        self._age = age         
    
    # Method
    def bark(self):
        return f"{self.name} says woof!"
    
    def get_age(self):
        return self._age

# Creating objects
my_dog = Dog("Buddy", 3)
print(my_dog.bark())
print(my_dog.species)

# String representation
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Pantoja", 37)
print(p)                    # Pantoja (37)
