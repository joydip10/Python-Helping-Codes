while True:
    try:
        age=int(input("A number: "))
    except ValueError:
        print("Value Error!!")
    except:
        print("Some other errors!!")
    else:
        print(f"Inserted Value: {age}")
        break
    finally:
        print("Finally!!!")
    
if age>18:
    print("You have the permission")
else:
    print("You don't have the permission")
    

#Exercise
    
    
def func(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Zero division Error!!")
    except TypeError as err:
        print(err)
    except:
        print("Some other errors!!")
    
    
print(func(36,9))




#Exercise

class AgeTooSmallError(ValueError):
    pass

age=int(input("Age: "))
if age>18:
    print("OK")
else:
    raise AgeTooSmallError("Age too small")
    