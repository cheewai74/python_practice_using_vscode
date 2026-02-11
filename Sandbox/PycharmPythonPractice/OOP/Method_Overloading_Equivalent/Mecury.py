class Mercury:
    def weight(self, w):
        print(w * 0.38)

class Mars:
    def weight(self, w):
        print(w * 0.38)

class Earth:
    def weight(self, w):
        print(w)

obj = Mercury()
print(obj.weight(50))
obj = Mars()
print(obj.weight(50))
obj = Earth()
print(obj.weight(50))

for obj in Mercury(), Earth(), Mars():
  print(obj.weight(50))