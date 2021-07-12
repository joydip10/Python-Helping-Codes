#other parameters
#args
#default parameter
#kwargs


def func(name,*args,defult_parameter="unknown",**kwargs):
    print(name)
    print(args)
    print(defult_parameter)
    print(kwargs)
    
dictt={str(i):("positive" if i>0 else "negative") for i in range(-5,6,1) if i!=0}
func("Joy",1,2,3,4,5,**dictt)


#Exercise-> using  args
l=["harshit","mohit"]

def func(reverse_str=False,*l):
    if reverse_str==False:
        p=[names.title() for names in l]
        return p
    else:
        p=[names[::-1].title() for names in l]
        return p

print(func(*l))
print(func(True,*l))

#Exercise -> using  Kwargs

l=["harshit","mohit"]

def func(**kwargs):
    if v in kwargs.values()==True:
        l