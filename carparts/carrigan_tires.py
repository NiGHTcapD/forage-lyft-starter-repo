from abc import ABC

from tire import Tire


class CarriganTires(Tire, ABC):
    def __init__(self, wheel_wear):
        wheel_wear = [0, 0, 0, 0]

    def tire_needs_service(self):
        max_wear = 0
        for x in wheel_wear:
            if x > max_wear:
                max_wear = x
        if max_wear < 0.9:
            return False
        else:
            return True
