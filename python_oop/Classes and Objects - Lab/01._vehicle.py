from typing import List


class Vehicle:

    def __init__(self, mileage: float, max_speed: float = 150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets: List[str] = []


# test code:
car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
