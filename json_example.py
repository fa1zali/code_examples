# Author: Faisal Ali
# Creation Date: 16-Nov-2020
# Version: 1.0

# Importing libraries
import json

# Creating a JSON payload
x = '{"name":"Faisal Ali", "age": 27, "city":"Gurugram"}'

# Parse JSON to Python
y = json.loads(x)
print(y) # JSON payload get converted to Python dictionary
print(type(y))
print(y['age'])
print("\n")

# Parse Python to JSON
a = {"name":"Faisal Ali", "age": 27, "city":"Gurugram"}
b = json.dumps(a)
print(b)
print(type(b))
print("\n")

# Coverting various Python datatypes to equivalent JSON
print(json.dumps({"name":"Faisal Ali", "age": 27})) # Dictionary >> Object
print(json.dumps(['Faisal Ali', 27])) # List >> Array
print(json.dumps(('Hello', 'there'))) # Tuple >> Array
print(json.dumps('Amazing')) # String >> String
print(json.dumps(27)) # Integer >> Number
print(json.dumps(31.46)) # Float >> Number
print(json.dumps(True)) # Boolean >> true
print(json.dumps(False)) # Boolean False >> false
print(json.dumps(None)) # None >> null
print("\n")

# Complex Example
c = {
    "name":"Harry",
    "age":30,
    "married":True,
    "divorced":False,
    "children":('Tom', 'Jerry'),
    "pets":None,
    "cars":[
        {"model":"Porsche Panamera", "kmpl": 15.1},
        {"model":"Lamboghini Aventador", "kmpl": 12.7}
    ]
}
print(json.dumps(c))
print("\n")
print(json.dumps(c, indent=4)) # For defining the number of indents
print("\n")
print(json.dumps(c, indent=4, separators=(".", "="))) # For changing the separators
print("\n")
print(json.dumps(c, indent=4, separators=(".", "="), sort_keys=True)) # For sorting the order of keys
print("\n")