#closures

def func(s):
    return s**2

p=func(2)
sqr=func


print(sqr(2))
print(p)
print(func(2))
print("Doc")
print(func.__name__)
print(sqr.__name__)

print("\n\n\n\n")


def out():
    def in_():
        print("Inside")
    return in_

out()()
ret=out()
ret()
ret #doesn't produce any output



print("\n\n\n\n\n")


def func(msg):
    def in_func():
        print(f"{msg} is the message from outer func")
    return in_func()


func("hey")




print("\n\n\n\n")


def to_pow(num):
    def inside(n):
        return n**num
    return inside

square=to_pow(2)
triad=to_pow(3)

print(square(3))
print(square(5))

print(triad(3))
print(triad(5))

