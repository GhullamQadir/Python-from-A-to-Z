import json

# Python dictionary
data = {
    "name": "Yash",
    "age": 18,
    "is_student": True ,
    "courses": ["Discrete Math", "Applied Calculus"],
    "address": None
}

# Convert to JSON string
json_string = json.dumps(data, indent=4)
print(json_string)

# Save to file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Parse JSON string
parsed = json.loads(json_string)
print(parsed["name"])

# Load from file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

# Working with custom objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_encoder(obj):
    if isinstance(obj, Person):
        return {"name": obj.name, "age": obj.age}
    raise TypeError("Object not serializable")

person = Person("Popatlal", 47)
json_str = json.dumps(person, default=person_encoder)
