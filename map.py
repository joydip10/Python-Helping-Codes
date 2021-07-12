l=[1,2,3,4,5]
def sqr(a):
    return a**2

p=[sqr(i) for i in l]


print(p)


squares=list(map(sqr,l))
print(squares)


squares=list(map(lambda a:a**2,l))
print(squares)



names=["harshit","vashishth","joy","dip","das","mohit"]

names_length=list(map(lambda a:len(a),names))
print(names_length)

names_length=map(len,names) #map object is iterable
print(names_length)
for i in names_length:
    print(i)
    

    

    