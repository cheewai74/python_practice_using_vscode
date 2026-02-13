import os
import hashlib

print(os.getcwd())

hash_object = hashlib.sha256(b'Hello World')
print(hash_object.hexdigest())