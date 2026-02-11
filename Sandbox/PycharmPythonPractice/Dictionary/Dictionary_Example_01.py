
ages = {
    "John": 34,
    "Matt": 23,
    "Natasha": 27,
    "Gabriella": 33
}

print(ages["John"])

ages.pop("John") # Remove a key value pair from dictionary

"""
    Dictionaries: Looping through keys
"""
customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St."
}

for each_key in customer_29876.keys():
    print(each_key)

for each_value in customer_29876.values():
    print(each_value)

for each_key, each_value in customer_29876.items():
    print("The customer's " + each_key + " is " + each_value)