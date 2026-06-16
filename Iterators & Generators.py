# Custom iterator
class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# Generator function
def countdown(start):
    while start > 0:
        yield start
        start -= 1

for num in countdown(5):
    print(num)          # 5, 4, 3, 2, 1

# Generator expression
squares_gen = (x**2 for x in range(1000000))  # Memory efficient

# Built-in iterators
my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))   # 1
print(next(iterator))   # 2
