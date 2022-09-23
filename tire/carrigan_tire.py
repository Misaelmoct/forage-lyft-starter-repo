from operator import truediv
from tire.tire import Tire 




class CarriganTire(Tire):

    def __init__(self, tires_worn_record):
        
        self.tire_worn_record = tires_worn_record


    def needs_service(self):
        
        for tire in self.tire_worn_record:

            if tire >= .9:
                return True

        return False