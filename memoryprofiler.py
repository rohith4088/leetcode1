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