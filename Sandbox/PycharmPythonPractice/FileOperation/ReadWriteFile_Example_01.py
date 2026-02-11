"""
    Example 1: Write to a file
"""
the_file = open("integers.txt", "w")
integers = [1, 2, 3, 4, 5]
for integer in integers:
    the_file.write(str(integer) + '\n')
the_file.close()

"""
    Example 2: Read a file
"""
the_file = open("integers.txt", "r")
lines = the_file.readlines()
for line in lines:
    print(line)
the_file.close()

greeting = "Hello, world!"
with open("greet.txt", "w") as f:
    f.write(greeting)
    f.close()

with open("greet.txt", "r") as f:
    text_of_file = f.read()
    f.close()

# Append
with open("greet.txt", "a") as f:
    f.write("\nHave a nice day!")
    f.close()

# CSV
import csv

with open("competitions.csv") as f:
    contents_of_file = csv.reader(f)

contents_of_f = csv.reader(f)
with open("competitions.csv") as f:
    reader_of_f = csv.reader(f)
    potter_competitions = []
    for each_line in contents_of_f:
        potter_competitions += each_line

# json
import json

alphabet_letters = ["a", "b", "c"]
with open("alphabet_list.json", "w") as f:
    json.dump(alphabet_letters, f)

# If you've defined a dictionary…
customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St.",
}

# …you save it the same way:
with open("customer_29876.json", "w") as f:
    json.dump(customer_29876, f)

# You begin by opening the file for reading, as usual:
with open("customer_29876.json") as f:
    customer_29876 = json.load(f)
    print(customer_29876)

# -------------------------------------------
try:
    filename = input("What text file to open? ")
    with open(filename) as f:
        print(f.read())
except FileNotFoundError:
    print("Sorry, " + filename + " not found.")