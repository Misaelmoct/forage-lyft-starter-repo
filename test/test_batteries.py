import unittest
from datetime import datetime


from battery.nubbin_battery import NubbinBattery
from battery.splinder_battery import SplinderBattery

###################################### Date Variables ##########################################
today = datetime.today().date()                                  
last_service_date_1year_ago = today.replace(year = today.year - 1) 
last_service_date_5year_ago = today.replace(year = today.year - 5) 
last_service_date_4year_ago = today.replace(year = today.year - 4)



class TestNubbin(unittest.TestCase):

    def test_battery_should_be_serviced(self):

        battery = NubbinBattery(last_service_date_5year_ago, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):

        battery = NubbinBattery(last_service_date_1year_ago, today)
        self.assertFalse(battery.needs_service())


class TestSplinder(unittest.TestCase):

    def test_battery_should_be_serviced(self):

        battery = SplinderBattery(last_service_date_4year_ago, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):

        battery = SplinderBattery(last_service_date_1year_ago, today)
        self.assertFalse(battery.needs_service())



if __name__ == '__main__':

    unittest.main()