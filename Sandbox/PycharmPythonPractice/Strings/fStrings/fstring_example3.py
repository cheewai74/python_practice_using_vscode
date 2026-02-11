# As shown below, fString is fastest. Should consider it as performance boost.

from string import Template

x, y = "Hello", "World"

print(f"{x} {y}")  # 39 nsec
print(x + " " + y)  # 43 nsec
print(" ".join((x,y)))  # 58.1 nsec
print("%s %s" %(x, y)) # 103 nsec
print("{} {}".format(x, y))  # 141 nsec
print(Template("$x $y").substitute(x=x, y=y))  # 1.24 usec , slow
