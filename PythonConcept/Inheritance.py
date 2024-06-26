class Contacts():
    all_contacts = []
    def __init__(self , email , phone):
        self.email = email
        self.phone = phone
        Contacts.all_contacts.append(self)
    def prints(self):
        for i in self.all_contacts:
            print(f'email:{i.email} , phone:{i.phone}') #accessing the objects using the dot operator
class Supplier():
    def __init__(self , order , email):
        self.order = order
        self.email = email
class ContactFactory():
    all_contacts = []
    @classmethod
    def create_contact(cls, email,  phone):
        contact = Contacts(email , phone)
        cls.all_contacts.append(contact)
        return contact
    @classmethod
    def create_supplier(cls ,order , email):
        supplier = Supplier(order , email)
        cls.all_contacts.append(supplier)
        return supplier
cf = ContactFactory()
cf.create_contact('rohiht@123' , '938928932')
cf.create_supplier('brake fluid' ,' rohith@123')

print("---------------")
#extending the built in's the list and dict methods
class LongestWord(dict):
    def calc(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest
dixt = LongestWord()
dixt['hello'] = 1
dixt['rohihth'] = 2
dixt['hellloooo'] = 3

print(dixt.calc())