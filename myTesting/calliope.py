from datetime import datetime

from abc import ABC
from car import Car
from capulet_engine import CapuletEngine
from nubbin import Nubbin
from tire import Tire
from brake import Brake


class Calliope(Car):
    

    def __init__(self, last_service_date, current_mileage, engine_last_service_mileage, tires_to_service, brake_last_service_miles):
        
        # engine = CapuletEngine(engine_last_service_mileage)
        # battery = Nubbin(last_service_date)
        # brake = Brake(brake_last_service_miles)
        super().__init__(current_mileage)
        self.engine = CapuletEngine(engine_last_service_mileage)
        self.battery = Nubbin(last_service_date)
        self.tire = Tire(tires_to_service)
        self.brake = Brake(brake_last_service_miles)
    
        

    def needs_service(self):
        
        bool = False
        for is_service_due in (self.engine, self.battery, self.tire, self.brake):

       
            if is_service_due.should_be_serviced(self):

                bool = True

        return bool




        # service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        # if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
        #     return True
        # else:
        #     return False
