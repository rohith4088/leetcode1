import concurrent.futures
import os 
from multiprocessing import Process , cpu_count
import time
import multiprocessing
# class MuchCpu(Process):
#     def run(self):
#         print(os.getpid())
#         for i in range(2000000000):
#             pass
# if __name__ == "__main__":
#     procs = [MuchCpu()for f in range(cpu_count())]
#     t = time.time()
#     for p in procs:
#         p.start()
#     for p in procs:
#         p.join()
#     print("the work took {} seconds".format(time.time() - t))
#example two for multiprocessing 
import multiprocessing
import time
import concurrent
# def do_something():
#     print("going to sleep for 1 second")
#     time.sleep(1)
#     print("done sleeping")
# processes = []
# if __name__ == "__main__":
#     start = time.perf_counter()
#     for _ in range(10):
#         p = Process(target = do_something)
#         p.start()
#         processes.append(p)
#     for process in processes:
#         process.join()
#     finish = time.perf_counter()
#     print("the time taken is {}".format(round(finish - start,2)))

#using process pool executors
# start = time.perf_counter()
# def do_something(seconds):
#     print(f'sleeping for {seconds} second(s)')
#     time.sleep(seconds)
#     return 'done sleeping.....'
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     secs = [5,4,3,2,1]
#     results = [executor.submit(do_something,1)for _ in range(10)]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
        

# finish = time.perf_counter()
# print("the time taken is {}".format(round(finish-start,2)))




from multiprocessing import Pool
# def f(x):
#     return x*x
# if __name__ == "__main__":
#     with Pool(5) as p:
#         print(p.map(f,[1,2,3,4]))



import os

# def info(title):
#     print(title)
#     print("parent",os.getppid())
#     print("child",os.getpid())
# def f(name):
#     print("hello",name)
# if __name__ == "__main__":
#     info("main_line")
#     p = Process(target = f , args = ['rohith'])
#     p.start()
#     p.join()


#multiprocessing supports three wayys to start a process--> fork , spawn , forkserver
#USING SPAWN

# def g(q):
#     q.put('hello')
# if __name__ == "__main__":
#     multiprocessing.set_start_method("spawn")
#     q = multiprocessing.Queue()
#     p = multiprocessing.Process(target = g,args = (q,))
#     p.start()
#     print(q.get())
#     p.join()


#USING CONTEXT_MANAGERS --> USED TO INITALISE MORE THAN ONE START METHOD IN THE SAME SCRIPT

def f(q):
    q.put("hello")
if __name__ == "__main__":
    ctx = multiprocessing.get_context("spawn")
    q = ctx.Queue()
    p = Process(target = f , args = (q,))
    p.start()
    print(q.get())
    p.join()

