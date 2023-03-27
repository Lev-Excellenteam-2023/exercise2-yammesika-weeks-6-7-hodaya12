"""

:param param1: this is function
:param param1: this is iterable of parameters for the function.
:returns: a dictionary which its keys are the returned values of the function
 and the values are list of parameters of the function
"""
def group_by(func,it):
    d={}
    for i in it:
        returned=func(i)
        if returned in d:
            d[returned].append(i)
        else:
            d[returned]=[i]
    return d


print(group_by(len, ["hi", "bye", "yo", "try"]))