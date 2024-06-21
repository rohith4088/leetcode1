# the self parameter id an omplict declarations used in class methods
# the act as the refrence to the object to which that particular method is called on

class Car:
    def __init__(self,brand , color):
        self.brand = brand
        self.color = color
    def check(self):
        return self.brand , self.color
    
my_car = Car("merc" , 'sclass') 
print(my_car.check())#the object my_car is passed as the self parameter to the method check()

