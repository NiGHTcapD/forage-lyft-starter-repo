from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self, battery_life):
        battery_life = 0