import json

data = {
    "name": "Piyush",
    "age": 21,
    "skills": ["Python", "SQL", "C++"]
}

# Write (dump) data to JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)  # indent=4 makes it readable

# Read (load) data back from JSON file
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data)
print(type(loaded_data))  # <class 'dict'>
