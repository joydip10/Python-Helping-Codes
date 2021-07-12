names=["harshit","vashishth","joy","dip","das","mohit"]

names_length=list(filter(lambda a:len(a)<5,names))
print(names_length)

for i in names_length:
    print(i)
    
    