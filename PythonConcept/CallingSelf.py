#the self parameter id an implict declarations used in class methods
#the act as the refrence to the object to which that particular method is called on

class Car:
    def __init__(self,brand , color):
        self.brand = brand
        self.color = color
    def check(self):
        return self.brand , self.color
    
my_car = Car("merc" , 'sclass') 
print(my_car.check())#the object my_car is passed as the self parameter to the method check()

#The __new__ constructor and the __init__ intializer
class MyClass():
    def __new__(cls , *args , **kwargs):
        print("creating new objects")
        return super().__new__(cls)  #call the parent classes new
    def __init__(self,value):
        print("initalising the object")
        self.value = value

myObject = MyClass("rohith")
print(myObject)

#Scenarios whre new override the __new__
#IMMUTABLE OBJECT SUBCLASSING
class UpperCaseString(str):
    def __new__(cls , value):
        return super().__new__(cls , value.upper())
    
s = UpperCaseString("rohith")
print(s)
print("-------------------------")



class uppercast(str):
    def __new__(cls , value):
        return super().__new__(cls , value.upper())