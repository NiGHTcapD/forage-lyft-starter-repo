from abc import ABC
# 
from battery import Battery


class SpindlerBattery(Battery, ABC):
    def __init__(self, battery_life):
        super().__init__(battery_life)
        battery_life = 3