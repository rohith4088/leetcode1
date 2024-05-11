#stack implemntation using linked list
#push--> O(1)
#pop-->O(1)
#lookup->O(1)--> see the top element

#create the node class node that will contain the data of the stacks and initialise the next pointer to the next node
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    def peek(self):
        if self.top is None:
            print("the stack seems to be empty")
        return self.top.data
    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
    def pop(self):
        if self.top == None:
            print("the stack seems to be empty")
        else:
            self.top = self.top.next
            self.length -= 1
            if(self.length == 0):
                self.bottom = None
    def printstack(self):
        if self.top == None:
            print("the stack seems to be empty")
        curr_node = self.top
        while(curr_node != None):
            print(curr_node.data)
            curr_node = curr_node.next

my_stack = Stack()
print(my_stack.peek())
#None

my_stack.push('hello')
my_stack.push('all')
my_stack.push('world')
my_stack.printstack()