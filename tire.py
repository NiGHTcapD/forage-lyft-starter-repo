from abc import ABC, abstractmethod


class Tire(ABC):
    def __init__(self, wheels):
        wheels = [0, 0, 0, 0]