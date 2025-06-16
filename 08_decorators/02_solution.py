def debug_function(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Function name: {func.__name__}")
        if args:
            print(f"Value of args is {args_value} and Total args is {len(args)}")
        if kwargs:
            print(f"Value of kwargs: {kwargs_value}")
        return result
    return wrapper

@debug_function
def example_function(n):
    return n*n

example_function(2)