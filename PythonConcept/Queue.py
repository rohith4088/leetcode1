import multiprocessing
from multiprocessing import Queue , Process

#implemntation of queues in multiprocessing
#for exvhanging objects between processes

def func(q):
    q.put([24,None,'name'])
if __name__ == "__main__":
    q = Queue()
    p = Process(target = func , args= (q,))
    p.start()
    print(q.get())
    p.join()
