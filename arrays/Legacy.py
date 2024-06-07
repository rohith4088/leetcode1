#array inplementation using dictionary
class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}
    def __str__(self):
        print(self.data.values())
        return str(self.__dict__)
    def get(self,index):
        return self.data[index]
    def push(self,item):
        self.data[self.length - 1] = item
        self.length += 1
    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item
    def insert(self,item,index):
        for i in range(self.length - 1,index , -1):
            self.data[i] = self.data[i-1]
        self.data[index] = item
        self.length += 1
    def delete(self,index):
        for i in range(self.length - 1,index):
            self.data[i] = self.data[i+1]
        del self.data[self.length - 1]
        self.length -= 1
arr = MyArray()
arr.push(1)
arr.push(2)
arr.push(3)
arr.push(4)
arr.push(5)
arr.push(6)
print(arr.get(3))

