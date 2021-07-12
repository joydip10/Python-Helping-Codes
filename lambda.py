add=lambda a,b : a+b
print(add(2,3))
add2=add
print(add2(2,3))
print(add) #prints address


def times(n):
    return lambda a: a*n

mydoubler= times(2)
mytripler= times(3)

print(mydoubler(5))
print(mytripler(5))


iseven= lambda a: a%2==0
print(iseven(5))


ret=lambda a,*args: [i**a for i in args]
print(ret(2,*[1,2,3,4,5]))

print(times(2)(3))
    