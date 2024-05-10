#implementaion of stacks in python is sinple and using arrays hence all the operation deon on arrays can be referenced for stacks
#ARRAY IMPLEMNTATION
class stack():
    def __init__(self,):
        self.array = []
    def peek(self):
        if len(self.array) == 0:
            print("the array is empty cannot peek")
        else:
            return self.array[len(self.array)-1]
    def push(self,data):
        self.array.append(data)
        return 
    def pop(self):
        if(len(self.array)) != 0:
            self.array.pop()
        else:
            print("stack is empty")
    def print_stack(self):
        if(len(self.array) == 0):
            print("the stack seems to be empty please add some elements")
        else:
            for i in range(len(self.array)-1,-1,-1):
                print(self.array[i])
        return
my_stack = stack()
my_stack.push("rohith")
my_stack.push("is")
my_stack.push("a")
my_stack.push("good boy")
my_stack.print_stack()


