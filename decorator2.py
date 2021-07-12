from functools import wraps

def decorator(func):
    ''' this is a decorator function '''
    @wraps(func)
    def wrapper(*args,**kwargs):
        ''' this is a wrapper function '''
        print("Inside the wrapper function: ")
        func(*args,**kwargs)
    return wrapper



@decorator
def func(s):
    ''' this is just a function '''
    print(f"Hello Buddy! {s}")
    



#f=decorator(func)
#f('joy')
    
    
func("JOY")

print(func.__doc__)


#Exercise
import time

def print_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t1=time.time()
        r=func(*args,**kwargs)
        t2=time.time()
        print(f"Time required to run this function->{func.__name__} is {t2-t1} ")
        return r
    return wrapper

@print_time
def add(*args):
    t=0
    for i in args:
        t=t+i
    return t

print(add(1,2,3))


#Exercise
def decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if all([type(arg)==int for arg in args]):
            return func(*args,**kwargs)
        else:
            return "Invalid d_type"
    return wrapper


@decorator
def func(*args):
    t=0
    for i in args:
        t+=i
    return t

print(func(1,2,3))
print(func(1,2,3.0))



























