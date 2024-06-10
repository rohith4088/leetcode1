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
start = time.perf_counter()
def do_something(seconds):
    print(f'sleeping for {seconds} second(s)')
    time.sleep(seconds)
    return 'done sleeping.....'
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something,1)for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
        

finish = time.perf_counter()
print("the time taken is {}".format(round(finish-start,2)))