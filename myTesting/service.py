from datetime import datetime

from calliope import Calliope


last_service_date = datetime.today().date()
current_mileage = 55001
last_service_mileage = 25000
tires = []
brake = 31000

car = Calliope(last_service_date, current_mileage, last_service_mileage, tires, brake)

print(car.needs_service())

