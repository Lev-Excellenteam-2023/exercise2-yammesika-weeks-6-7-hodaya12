import functools
"""
This decorator factory gets a type as a parameter and checks if the argument function is in this type 

:param param1: this is the type
:returns: returns the decorator
:raises keyError: raises an exception if the type is not correct
"""
def type_check(correct_type):
    def decorator(fn):
        @functools.wraps(fn)
        def inner(arg):
            try:
                if type(arg)!=correct_type:
                    raise Exception('the type of the parameter is not correct')
                return fn(arg)
            except Exception as e: return e
        return inner
    return decorator

@type_check(int)
def times2(num):
    return num*2

print(times2(8))
print(times2(8.7))
print(times2.__name__)