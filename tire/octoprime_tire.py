from tire.tire import Tire





class OctoprimeTire(Tire):

    def __init__(self, tires_worn_record):

        self.tires_worn_record = tires_worn_record


    def needs_service(self):

        sum = 0
        for tire in self.tires_worn_record:

            sum += tire

        return sum >= 3
