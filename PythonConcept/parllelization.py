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
