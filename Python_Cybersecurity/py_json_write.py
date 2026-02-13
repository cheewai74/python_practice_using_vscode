import json

json_data = '''{
    "name": "Mos",
    "age": 41,
    "city":"Singapore Central",
    "weapons":["bo staff", "sword","dagger"]
}'''

json_string = json.dumps(json_data, indent=4)
print(json_string)

with open('data.json','w') as file:
    json.dump(json_data, file, indent=4)