import functools

"""
This decorator executes the function it wraps twice. 

:param param1: this is the function that decorated
:returns: returns the wrapper
"""
def twice_func_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        func(*args, **kwargs)
    return wrapper



@twice_func_decorator
def times2(num):
    print(num*2)

times2(5)
