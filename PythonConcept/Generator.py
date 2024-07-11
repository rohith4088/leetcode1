#A CODE THAT EXPLAINS THE WORKING OF GENERATORS
#LETTS FIRST UNDERSTAND THE NEED FOR A GENERATOR PATTERN
#consider this fucntion 
from memory_profiler import memory_usage , profile

file_log = open("memeory.log" , 'w+')

@profile(stream = file_log)
def gen(n):
    num , nums = 0, []
    while num < n:
        nums.append(n)
        num +=1 
    return nums

gen(10000)

#this code has a memory usage oof around 45MiB which us not great ,  becayse the whole 1000 numbers
# are stored in the memory
#we do not want that
import sys
#hence we use generator
def my_generator(n):
    num , nums = 0 , []
    while num < n:
        nums.append(n)
        yield nums
        num += 1
    return nums

values = my_generator(10000)
print(sys.getsizeof(values))
print(next(values))
print(next(values))
print(next(values))

print("-------------------------------")

#THE GOOD OLD OOPS PATTERN (GENERATOR PATTERN)
class first_n(object):
    def __init__(self , n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self
    def __next__(self):
        return self.next()
    def next(self):
        if self.num < self.n:
            cur , self.num = self.num , self.num + 1
            return cur
        raise StopIteration()
sums = sum(first_n(1000000))
    
print(sums)

#LETS CRASH THE SYSTEEM
# def infinite_sequence():
#     result = 1
#     while True:
#         yield result
#         result *= 5
# values = infinite_sequence()
# for x in values:
#     print(x)


d1={"a":1,'b':2,'c':3,'d':4}
d2 = {'d':4,'e':5,'f':6}

combined_dict = {**d1 , **d2}
print(combined_dict)