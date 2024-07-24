#DATA MANIPULATION USING ASSERTION 

def DataProcessing(data , **kwargs):
    assert 'id' in data , "id not found in data"

    assert 'name' in data , "name not found in data"

    pass


print(DataProcessing({"id" : 1 , "name" : "rohith"}))


#ALGORITHMIC INPLEMNTATION OF EXCEPTION HANDLING IN PYTHON

# def get_value_from_dict(data , key):
#     try:
#         value = data[key]
#     except KeyError:
#         print("the key {key} was not found")
#         value = None
#     return value



#defining your own exceptrion

class InvalidWithdrawal(Exception):
    def __init__(self , amount , balance):
        super().__init__("your balance is more than your withdrwarl amount")
        self.amount = amount
        self.balance = balance

    def overage(self):
        self.balance = self.amount

raise InvalidWithdrawal(25 , 24)



