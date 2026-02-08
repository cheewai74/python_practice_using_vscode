from dataclasses import dataclass

@dataclass
class Point:
    lat: float
    long: float
    
print(Point.__annotations__)
print(Point(1,2))