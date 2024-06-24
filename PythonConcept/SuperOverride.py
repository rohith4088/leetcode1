#super and override method
# Overriding
# means altering or replacing a method of the superclass with a new method (with
# the same name) in the subclass.
#super
# super function does; it returns the object as an
# instance of the parent class, allowing us to call the parent method directly:

#this is overiding
class Contacts():
    all_contacts = []
    def __init__(self , email , phone):
        self.email = email
        self.phone = phone
        Contacts.all_contacts.append(self)
    def prints(self):
        for i in self.all_contacts:
            print(f'email:{i.email} , phone:{i.phone}')

class FreindList(Contacts):
    def __init__(self, email , phone,name):
        self.email = email
        self.phone = phone
        self.name = name
# WHY USE SUPER METHOD INSTEAD OF JUST OVERRIDING 
#Our Contact and Friend classes
# have duplicate code to set up the name and email properties; this can make code
# maintenance complicated as we have to update the code in two or more places.
# More alarmingly, our Friend class is neglecting to add itself to the all_contacts
# list we have created on the Contact class.
#this is using the super method

class FriendlistUsingSuper(Contacts):
    def __init__(self,email , phone , name):
        super().__init__(email , phone)
        self.name = name

        

#ADVANCED SUPER AND OVERRIDE
#COOPERATICE MTTHOD CALLS
from datetime import datetime
class BaseLogger:
    def log(self , message):
        print(f'Base : {message}')
class TimeStampLogger(BaseLogger):
        def log(self,message):
            super().log(message)
            print(f"TimeStamp : {datetime.now()}")

logger = TimeStampLogger()
logger.log("An important event occurred.")


#meta class interaction
#Metaclasses Define Classes: Just as a class defines how instances are created and behave, a metaclass defines how classes are created and behave. It's a "class factory" that controls the construction of classes.
class MyMetaclass(type):
    def __new__(metacls, name, bases, namespace):
        print(f'Creating class name of {name}, bases {bases} and attributes {namespace}')
        return super().__new__(metacls, name, bases, namespace)

class MyClass(metaclass=MyMetaclass):
    x = 10

    def __init__(self, y):
        self.y = y
# metacls: A reference to the metaclass itself.
# name: The name of the class being created.
# bases: A tuple of the base classes of the class being created.
# namespace: A dictionary containing the attributes (variables and methods) of the class.