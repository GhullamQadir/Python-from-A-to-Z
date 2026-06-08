# For loop
for i in range(5):
    print(i)                # 0, 1, 2, 3, 4

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for num in range(10):
    if num == 3:
        continue            # Skip 3
    if num == 7:
        break               # Stop at 7
    print(num)

# Else with loops
for i in range(3):
    print(i)
else:
    print("Loop completed!")  # Runs if no break

# Enumerate & Zip
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

names = ["Faizan", "Sikandar"]
scores = [95, 87]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
