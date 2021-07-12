l1=[1,3,5,7]
l2=[2,4,6,8]
l3=[]
l3.extend(l1)
l3.extend(l2)
l3.sort()
print(l3)

#all
if all([nums%2==0 for nums in l3]):
    print("True")
else:
    print("False")
    
if all([nums%2==0 for nums in l1]):
    print("True")
else:
    print("False")

if all([nums%2==0 for nums in l2]):
    print("True")
else:
    print("False")

print("\n\n\n")

#any
if any([nums%2==0 for nums in l3]):
    print("True")
else:
    print("False")
    
if any([nums%2==0 for nums in l1]):
    print("True")
else:
    print("False")

if any([nums%2==0 for nums in l2]):
    print("True")
else:
    print("False")
    
    
    
    
#Exercise
print("\n\n\nExercise:")
def func(*args):
    t=0
    for i in args:
        t=t+i
    return t

print(func(*[i for i in range(1,11)]))


def func(*args):
    t=0
    if all([type(i)==int or type(i)==float for i in args]):
            for i in args:
                t=t+i
            return t

    else:
        return "non sumable data types are present\n"


print(func(*[1,2.0,"string"]))
print(func(*[1,2.0,3]))  
print(func([1,2.0,3]))    #because we haven't unpacked the list



def all_func(*args):
    t=0
    for i in args:
        if type(i)==list:
            for j in i:
                t+=j
        elif type(i)==tuple:
            for j in i:
                t+=j
        elif type(i)==set:
            for j in i:
                t+=j
        else:
            t=t+i
        
    return t

print(all_func(*[1,2.0,[1,2,3]]))