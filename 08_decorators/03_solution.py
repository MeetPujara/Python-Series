import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        start = time.time()  # start timer
        
        if args in cache_value:
            result = cache_value[args]
            print(f"⏱️ Cached result returned in {time.time() - start:.3f} seconds")
            return result
        
        result = func(*args)
        cache_value[args] = result
        
        print(f"⏱️ Computed result in {time.time() - start:.3f} seconds")
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a + b

print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(5,3))
print(long_running_function(7,3))