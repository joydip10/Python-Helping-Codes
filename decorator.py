def decorator(func):
    def wrapper():
        print("Inside wrapper:")
        func()
    return wrapper


@decorator
def func1():
    print("This is first function")

@decorator    
def func2():
    print("This is the second function")
    
#def decorator(func):
#    print("Inside The Decorator:")
#    func()


#var=decorator(func1)
#var()

print("Calling function1 with decorator attached on the top: \n")
func1()
print("\n")

print("Calling function2 with decorator attached on the top: \n")
func2()
print("\n")
