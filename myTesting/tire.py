


from operator import truediv


class Tire():

    def __init__(self, tires_to_service):
        self.tires_to_service = tires_to_service

    def should_be_serviced(self, car):

        if len(self.tires_to_service) > 0:
            return True

        else:
            return False
        
        