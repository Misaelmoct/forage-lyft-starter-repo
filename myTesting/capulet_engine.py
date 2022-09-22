from abc import ABC


class CapuletEngine():

    service_frequency_in_miles = 30000

    def __init__(self, engine_last_service_mileage):
        # super().__init__(last_service_date)
        self.engine_last_service_mileage = engine_last_service_mileage


    def should_be_serviced(self, car):
        return car.current_mileage - self.engine_last_service_mileage > self.service_frequency_in_miles
