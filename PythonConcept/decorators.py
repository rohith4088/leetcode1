import time

def timeit(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        result = func(*args , **kwargs)
        end = time.time()
        print(f'time taken by {func.__name__} is {end - start}')
        return result
    return wrapper

@timeit
def compute(n):
    time.sleep(n)
    return n

result = compute(4)
print("result-->",result)

