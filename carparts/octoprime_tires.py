from abc import ABC

from tire import Tire


class OctoprimeTires(Tire, ABC):
    def __init__(self, wheel_wear):
        wheel_wear = [0, 0, 0, 0]

    def tire_needs_service(self):
        total_wear = 0
        for x in wheel_wear:
            total_wear = total_wear + x
        if total_wear < 3.0:
            return False
        else:
            return True
