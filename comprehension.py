#list compehension
l=[i for i in range(1,11)]
print(l)

#exercise

def func(l):
    p=[names[::-1] for names in l]
    return p

l=["kala","gohin","pola"]
print(func(l))


even_nums=[i for i in range(1,11) if i%2==0 ]
print(even_nums)

#exercise

l=["string","integer",[1,2,3],1.0,1,2]
n_l=[str(i) for i in l if( type(i)==float or type(i)==int) ]
print(n_l)


nums=[i if i%2!=0 else i*2 for i in range(1,11)]
print(nums)

print('this one')
nums=[[i for i in range(5)] for j in range(5)]
print(nums)

nums=[i**2 for i in range(1,11) if i%2==0]
print(nums)

nums=[i if i%2==0 else -i for i in range(1,11)]
print(nums)

nums=[i if i%2==0 else -i for i in range(-2,11) if i!=0]
print(nums)

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")




#Dictionary comprehension
names="JOY DIP DAS"
name_dict={i:names.count(i) for i in names if i!=" "}
val_dict={i:("even" if i%2==0 else "odd") for i in range(1,11)}
print(name_dict)
print(val_dict)



#set comprehension
s={i for i in range(1,11) if i%2==0}
print(s)
s={f"even: {i}" if i%2==0 else f"odd: {i}" for i in range(1,11)}
print(s)
