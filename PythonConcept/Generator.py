#A CODE THAT EXPLAINS THE WORKING OF GENERATORS
#LETTS FIRST UNDERSTAND THE NEED FOR A GENERATOR PATTERN
#consider this fucntion 
# from memory_profiler import memory_usage , profile

# file_log = open("memeory.log" , 'w+')

# @profile(stream = file_log)
# def gen(n):
#     num , nums = 0, []
#     while num < n:
#         nums.append(n)
#         num +=1 
#     return nums

# gen(10000)

#this code has a memory usage oof around 45MiB which us not great ,  becayse the whole 1000 numbers
# are stored in the memory
#we do not want that

#hence we use generator
def my_generator(n):
    num , nums = 0 , []
    while num < n:
        nums.append(n)
        yield nums
        num += 1
    return nums

values = my_generator(10000)
print(next(values))
print(next(values))
print(next(values))


#THE GOOD OLD OOPS PATTERN (GENERATOR PATTERN)

