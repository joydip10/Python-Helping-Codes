#set

s={1,2,3,4,3,3}
print(s)


#adding
s.add(5)
print(s)

#removing
s.remove(3)
print(s)


# if we use remove(90) it will generate error since there is no such element as 90 but is case of using discard() method if there is 90 it will be deleted otherwise no error will be generated
s.discard(90)


k=s.copy(); #copies the items

print(k);

s.clear() #clears the set

if(len(s)==0):
    print("clear")
else:
    print("not cleared")


print(k)



#union
s1={1,2,3}
s2={3,4,5}
print(s1|s2)

#intersection
print(s1 & s2)
