import unittest


from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire



######################### values ##############################

tires_worn_record_new = [0.1, 0.2, 0.3, 0.4]
tires_worn_record_carrigan = [0.9, 0.7, 0.8, 0.6]
tires_worn_record_octoprime = [1, 1, .5, .5]

class TestCarrigan(unittest.TestCase):

    def test_tires_should_be_serviced(self):

        tire = CarriganTire(tires_worn_record_carrigan)
        self.assertTrue(tire.needs_service())

    def test_tires_should_not_be_serviced(self):

        tire = CarriganTire(tires_worn_record_new)
        self.assertFalse(tire.needs_service())



class TestOctoprime(unittest.TestCase):

    def test_tires_should_be_serviced(self):

        tire = OctoprimeTire(tires_worn_record_octoprime)
        self.assertTrue(tire.needs_service())

    def test_tires_should_not_be_serviced(self):

        tire = OctoprimeTire(tires_worn_record_new)
        self.assertFalse(tire.needs_service())