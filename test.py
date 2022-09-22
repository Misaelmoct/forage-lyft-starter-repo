from datetime import datetime
from car import Car

from car_factory import CarFactory


today = datetime.today().date()
last_service_date = today.replace(year=today.year - 5)
current_mileage = 0
last_service_mileage = 0

print(today, last_service_date, current_mileage, last_service_mileage)

factory = CarFactory()
car1 = factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
car2 = factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
car3 = factory.create_palindrome(today, last_service_date, False)
car4 = factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
car5 = factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)

print("Callipe:", car1.needs_service()) #30000 miles 2 years
print("Glissade:", car2.needs_service()) # 60000 miles 2 years
print("Palindrome:", car3.needs_service()) # light on 2 years
print("Rorschach:", car4.needs_service()) # 60000 miles 4 years
print("Thovex:", car5.needs_service()) # 30000 miles 4 years



