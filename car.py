from abc import ABC
from serviceable import Serviceable

class Car(Serviceable, ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        for service in (self.engine, self.battery):

            if service.needs_service():

                return True

        return False
