def total(*nums):
    total=0
    print("Type of *nums: "+str(type(nums)))
    print("Packed as tuple: ")
    print(nums) #packed
    print("Unpacked: ")
    print(*nums) #unpacked
    for i in nums:
        total+=i
    return total

print(total(1,2,3,4,5,6,7,8,9,10))
print("\n\n\n\n\n")

l=[i for i in range(1,11)]
t=(i for i in range(1,11))
s={i for i in range(1,11)}

print("\n\n\n\n\n")
print("When the input is as list:  ")
print(total(*l))

print("\n\n\n\n\n")
print("When the input is as tuple:  ")
print(total(*t))

print("\n\n\n\n\n")
print("When the input is as set:  ")
print(total(*s))




#Exercise

l=[i for i in range(1,4)]
def func(num,*args):
    if args:
        l=[i**num for i in args]
        return l
    else:
        return "You didn't put anything inside!!"
        
print(func(3,*l))
print(func(3,*[2,3,4]))
print(func(3))

print("\n\n\n\n\n\nExercise:")
def func(*args):
    print(*args)
    print(args)
    summ=0;
    for i in args:
        summ=summ+i
    return summ


def func1(*args):
    print(*args)
    print(args)
    summ=0;
    for i in args:
        p=0;
        for j in i:
           p=p+j
        summ=summ+p
    return summ


print(func(1,2,3,4,5))
print('\n\n\n')
print(func1([1,2,3],[4,5,6],[7,8,9,10]))

