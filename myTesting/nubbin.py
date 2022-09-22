from datetime import datetime



class Nubbin():

    def __init__(self, last_service_date):

        self.last_service_date = last_service_date
        self.service_frequency_in_years = 4

    def should_be_serviced(self, car):
        #if the days since last_service_date are greater or 
        # equal than service frequency return true otherwise false
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + self.service_frequency_in_years)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False