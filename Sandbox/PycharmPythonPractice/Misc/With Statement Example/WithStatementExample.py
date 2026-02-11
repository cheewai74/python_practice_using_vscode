"""
f=open('hello.txt','w')
try:
    f.write('hello , world')
finally:
    f.close()

Python will automatically close the file with "with" statement

"""
with open('hello.txt', 'w') as f:
    f.write("Hello, World!")

from contextlib import contextmanager


@contextmanager
def managed_file(name):
    try:
        f = open(name,'w')
        yield f
    finally:
        f.close()


with managed_file('hello.txt') as f:
    f.write('Hello Moses!\n')
    f.write("Tomorrow lunch")
