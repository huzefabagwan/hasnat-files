"""
Dictionary in Python
Definition
A dictionary in Python is a collection of key-value pairs.
 It stores data in the form of key: value. Dictionary is ordered, changeable (mutable), 
 and does not allow duplicate keys.

Example:
student = {    "name": "Huzefa",    "age": 20,    "city": "Bhusawal"}



2. Syntax
dictionary_name = {"key1": "value1", "key2": "value2"}



- Key: Used to identify the data.
- Value: The data stored against a key.
3. Important Dictionary Methods
Method	Use
keys()	Returns all keys
values()	Returns all values
items()	Returns key-value pairs
get()	Returns the value of a key
update()	Adds or updates items
pop()	Removes a specified key
clear()	Removes all items
copy()	Creates a shallow copy

"""

empty_dict = {}


names = {
    # key  [          value                ]
    "name":["hansat" , "uazir" , "mudassir"] ,
    "Phone_number" : 9765619091 ,
    "percentage": 89.7 , 
    56:{
        "pin":7894
    },
    "hotel_name": "KFC"
}

# print(names.values())
# print(names.keys())
# print(names.items())
# print(names.get("name"))
# print(names.get("marks" , 1))



# copy_names = names.copy()
# print(copy_names.clear())
# print(names)

names.update({"marks":245})
names.update({"age" : 20 , "city":"Bhusawal" })
names.update({"pin": 4561})
print(names)

