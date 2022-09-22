from abc import ABC, abstractmethod
from tire import Tire
from brake import Brake

class Car(ABC):
    def __init__(self, current_mileage):
        self.current_mileage = current_mileage
        # self.engine = engine
        # self.battery = battery
        # self.tire = Tire(tires_to_service)
        # self.brake = brake

    @abstractmethod
    def needs_service(self):
        pass
