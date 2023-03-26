# import OOP.classes
import time
import pytest
from OOP.classes import Motorcycle, Car

moto = Motorcycle("Jim","Harley")
car = Car("Honda","Civic")

for vehicle in [moto, car]:
    print(vehicle)
    vehicle.turn_engine_on()
    vehicle.turn_headlight_on()
    vehicle.start_driving()
    vehicle.turn('left')
    vehicle.turn('right')
    print(vehicle)
    vehicle.stop_driving()
    vehicle.turn_engine_off()
    vehicle.turn_headlight_off()
    print()
    time.sleep(1)