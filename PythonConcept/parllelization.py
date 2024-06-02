from multiprocessing import cpu_count , Process
import time
import os

class memory(Process):
    def run(self):
        print(os.getpid())
        for f in range(200000000):
            pass
if __name__ == "__main__":
    procs =[memory() for f in range(cpu_count())]
    t = time.time()
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print('work took {} seconds'.format(time.time() - t))


class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0
    def insert(self,data):
        new_node = Node(data)
