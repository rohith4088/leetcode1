from memory_profiler import profile,memory_usage
#file_log = open("memory_profiler.log","w+")

@profile#stream = file_log)
def myfucn(list_size):
    l1 = ['hello'] * list_size
    l2 = ['world'] * list_size
    del l2
    return l1
myfucn(1000000)
myfucn(1000)
myfucn(1000000000)


#mprof run --python main.py
#mprof plot


# def f1():
#     print("f1 is called")
# def f2(f):
#     f()
# f2(f1)

#pyhton decorators
def f1(func):
    def wrapper(*args,**kwargs):
        print("started")
        func(*args,**kwargs)
        print("ended")
    return wrapper
@f1
def f(a,b = 9):
    print(a,b)
#f1(f)()
#or
#x = f1(f) #decoraters
f("hello")
