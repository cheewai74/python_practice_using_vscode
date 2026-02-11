"""
my_mapping = {'a': 23, 'b':42, 'c':0xc0ffee}
my_mapping
"""
import json

my_mapping = {'a': 23, 'b':42, 'c':0xc0ffee}
print(json.dumps(my_mapping, indent=4, sort_keys=True))