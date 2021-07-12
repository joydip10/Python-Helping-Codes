#BUILT-IN ERRORS

########SYNTAX ERROR->


# def func: -----> () missing
#     pass


######## indentation errors
######## name errors (variable names)
######## type errors(like adding two variables of different data types)
######## index error(index out of range etc etc)
######## value error(like assigning wrong values to wrong data types)
######## attribute error(using methods or attributes which is not present)
######## key error( like using wrong key of dictionary)



#Raising Errors

def func(a,b):
    if(type(a)==int and type(b)==int):
        return a+b
    else:
        raise TypeError("Wrong Data Type Inserted\n")
        
        
print(func(1,2))
print(func('1','2'))


