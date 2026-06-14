# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement")

# Child classes
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Polymorphism
animals = [Dog("Buddy", "Golden"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())

# Checking inheritance
print(isinstance(Dog("Buddy", "Golden"), Animal))   # True
print(issubclass(Dog, Animal))                      # True

# Multiple inheritance
class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Animal, Flyer, Swimmer):
    def speak(self):
        return "Quack!"
