import time

"""

:param param1: this is the function
:param param2: this is the parameters of the function if they are given by position
:param param3: this is the parameters of the function if they are given by name
:returns: the execution time of the function
"""
def timer(func,*args,**kwargs):
    if(args==() and kwargs=={}):
        starttime = time.time()
        func(*args)
        endtime = time.time()
    elif args==():
        starttime = time.time()
        func(**kwargs)
        endtime = time.time()
    else:
        starttime = time.time()
        func(*args)
        endtime = time.time()
    return endtime-starttime

print(timer(print, "Hello"))
print(timer(zip, [1, 2, 3], [4, 5, 6]))
print(timer("Hi {name}".format, name="Bug"))

