



class Brake():


    def __init__(self, brakes_last_service_miles):

        self.service_frequency_in_miles = 30000
        self.brakes_last_service_miles = brakes_last_service_miles




    def should_be_serviced(self, car):

        return car.current_mileage - self.brakes_last_service_miles > self.service_frequency_in_miles
