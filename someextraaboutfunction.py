def func(a,b):
    ''' it is a function which has two inputs and returns one output'''
    return a+b

# this method is called docc string
    #-> helps others to understand better about a function
    

print(func.__doc__)  #prints the doc string
print(len.__doc__)
print(help(len))