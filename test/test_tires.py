import unittest
from datetime import datetime

from carparts.carrigan_tires import CarriganTires
from carparts.octoprime_tires import OctoprimeTires


class TestCarrigan(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        wheel_wear = [0, 0, 0, 0.9]

        carpart = CarriganTires(wheel_wear)
        self.assertTrue(car.tire_needs_service())

    def test_tires_should_not_be_serviced(self):
        wheel_wear = [0.8, 0.8, 0.8, 0.8]

        carpart = CarriganTires(wheel_wear)
        self.assertFalse(car.tire_needs_service())

class TestOctoprime(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        wheel_wear = [0.6, 0.7, 0.8, 0.9]

        carpart = OctoprimeTires(wheel_wear)
        self.assertTrue(car.tire_needs_service())

    def test_tires_should_not_be_serviced(self):
        wheel_wear = [0.8, 0.7, 0.6, 0.5]

        carpart = OctoprimeTires(wheel_wear)
        self.assertFalse(car.tire_needs_service())



if __name__ == '__main__':
    unittest.main()
