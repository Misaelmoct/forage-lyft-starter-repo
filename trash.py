from datetime import datetime
from datetime import date
from time import strftime

class Car:
    
    def __init__(self, color, mileage):

        self.color = color
        self.mileage = mileage


    def getColor(self):
        
        return f"The car's color is {self.color}"

    def getMileage(self):

        return f"The car's mileage is {self.mileage}"






car1 = Car("red", 60000)
car2 = Car("blue", 10000)

# print(car1.getColor())
# print(car2.getMileage())


date1 = date(2022, 9, 19)
date2 = datetime.today().date()


print( strftime(str1 , date2 - date1))