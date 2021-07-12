def func(n):
    if n==1:
        return 1
    if n==0:
        return 0
    
    return func(n-1)+func(n-2)


print(func(3))


def func(age=None,name="unknowm"):
    print(f"Age: {age}")
    print(f"Name: {name}")
    
func(23)

