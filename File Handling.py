# Writing to file
with open("test.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line")

# Reading from file
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("test.txt", "r") as file:
    for line in file:
        print(line.strip())

# Append mode
with open("test.txt", "a") as file:
    file.write("\nAppended line")

# Read specific lines
with open("test.txt", "r") as file:
    lines = file.readlines()    # Returns list

# Working with CSV
import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Laila", 23])

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
