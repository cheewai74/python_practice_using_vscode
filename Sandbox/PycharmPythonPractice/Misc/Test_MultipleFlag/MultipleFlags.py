"""
    Different ways to test multiple flags at once.
"""

x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print("Passed")

if 1 in (x, y, z):
    print("Passed")

if x or y or z:
    print("Passed")

if any((x, y, z)):
    print("Passed")