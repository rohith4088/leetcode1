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

        

