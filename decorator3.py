from functools import wraps

def data_type(d_t):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            if all([type(arg)==d_t for arg in args]):
                return func(*args,**kwargs)
            else:
                return "Invalid data type"
            
        return wrapper
    return decorator


@data_type(int)
def func(*args):
    t=0
    for i in args:
        t+=i
    return t

@data_type(str)
def add(*args):
    t=""
    for i in args:
        t+=i
    return t

print(func(1,2,3,4))
print(func(1,2,3,"str"))

print(add("1","2","3","4"))
print(add("1","2","3",4))
        
    