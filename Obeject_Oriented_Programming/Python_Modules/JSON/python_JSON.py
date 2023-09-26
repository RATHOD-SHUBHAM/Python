'''
    JSON: Javascript Object Notation.
    Serialization: The process of converting a data structure into a format that can be stored is called serialization.
    Deserialization: Deserialization is the process of converting data from the json format to ‘python readable’ data types.
    Docs: https://docs.python.org/3/library/json.html
'''

# Todo: Deserilization
'''
    Deserialization gets taken care of with the json module’s load( ) and loads( ) functions.
    
    There’re two methods available in the Python json module to handle the deserialization process:

        * load() – converts a JSON formatted stream to a Python object
        * loads() – converts a JSON formatted string to a Python object
'''

import json
with open("deserialize.json","r") as file:
    jsonData = json.load(file)
    # jsonData = json.loads(s) # takes in str,byte or bytes
print("Datatype of variable: ", type(jsonData))

for i in jsonData:
    print(i , jsonData[i])


# Todo: Read Json

import json

# We can straight away open the json file in 'read' mode,
# the way we do it with .txt and .csv files
with open("example.json", "r") as file:
    jsonData = json.load(file)

print("Type of JSON Object: ", type(jsonData))

# Traversing the json file
for name in jsonData:
    print("Name: ", name)
    print("Phone Number: ", jsonData[name]["number"])
    print("Age: ", jsonData[name]["age"])

    print("Address:")
    for line in jsonData[name]["address"]:
        print(line)
    print()

# Todo: Serilizing: Create JSON file

'''
    There’re two methods available in the Python json module to handle the serialization process:

        * dump() – converts Python object as a JSON formatted stream (usually used to save JSON data to the file)
        * dumps() – converts Python object as a JSON formatted string (produces a Python string object which contains JSON data)
'''

data = {
    "Person": {
        "name": "Shubham Rathod",
        "Like": "Car"
    }
}

with open('dummy.json', "w") as f:
    # json.dump(data, f, indent = 2) # dumps to file
    json.dumps(data, indent = 2, sort_keys= True)