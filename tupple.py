t=("pine-apple",)
print(t)
p=("apple","banana","orange","orange")
print(p)
#We can't add or remove or change anything in tuple because its immutable

print(t+p)

k=t+p;
print(k)

for i in k:
    print(k.count(i))
    
    
#TO change anything or to ad , remove any element in tuples we first convert it to a list and then change the list before we retransform it to a list
    
#tuple unpacking
guiterists=("Michael","Jordan","Stuart")
g1,g2,g3=guiterists
print(g1)
print(g2)
print(g3)

number=(1,2,3)
print(max(number))
print(min(number))