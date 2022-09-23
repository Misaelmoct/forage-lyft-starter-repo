import unittest


from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine




##################################### Mileage Variables ########################################
last_service_mileage = 0
# last_service_mileage_old_car = 70000
current_mileage_new_engine = 1000
current_mileage_old_capulet = 30001
current_mileage_old_willoughby = 60001


###################################### Light Signal Variables ######################################
light_is_on = True
light_is_off = False


class TestCapulet(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        
        engine = CapuletEngine(current_mileage_old_capulet, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):

        engine = CapuletEngine(current_mileage_new_engine, last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestWilloughby(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        
        engine = WilloughbyEngine(current_mileage_old_willoughby, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):

        engine = WilloughbyEngine(current_mileage_new_engine, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternman(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        
        engine = SternmanEngine(light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):

        engine = SternmanEngine(light_is_off)
        self.assertFalse(engine.needs_service())



if __name__ == '__main__':

    unittest.main()