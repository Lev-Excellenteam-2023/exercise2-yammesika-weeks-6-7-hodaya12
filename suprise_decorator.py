import functools

"""
This decorator prints surprise! instead doing original functionality

:param param1: this is the function that decorated
:returns: returns the wrapper
"""
def surprise_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('surprise!')
    return wrapper


@surprise_decorator
def times2(num):
    return num*2

print(times2(5))