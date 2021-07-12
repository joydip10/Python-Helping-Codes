l=[];
l.append("Apple")
l.append("Banana")
l.append("Pine-apple")
l.append("Coconut")
l.append("Mango")
print(l)

l.insert(1,"Orange")
print(l)

l[1]="ORANGE"; #portrays changeablity of lists
print(l)

l.remove("Coconut")
print(l)

del l[2]
print(l)

l.clear()
print(l)


l.append("Apple")
l.append("Banana")
l.append("Pine-apple")
for i in l:
    print(i,end=" ")
print("\n")

n_l=list(); #or we can declare a list by l=[]
n_l=l #or we can do this at the time of declaration of n_l by n_l=list(l)
print(n_l)

del l
#print(l) #produces error since the list l has been completely deleted from the memory


an_l=["kola","apel","am"]
print(n_l+an_l)
n_l.append(an_l)
print(n_l)
an_l.extend(an_l)
print(an_l)  #same as adding two lists usins + operator



an_l.reverse()
print(an_l)

print("\n")


for i in an_l:
    print(f"Count of\"{i}\" in the list an_l: {an_l.count(i)}")
    
    
user_info=["Kola","khay","babuta"]
print(",".join(user_info))
print(" ".join(user_info))
print("*".join(user_info))   



list_range=list(range(1,11))
print(list_range)



#Exercise

numbers=[1,2,3,4,5]
def func(numbers):
    p=[]
    for i in numbers:
        p.append(i**2)
    return p

print(func(numbers))




#Exercise

names=["abc","xyz","klm","d"]
def func(names):
    rev=[]
    for i in names:
        rev.append(i[::-1])
    return rev   

print(func(names))


#Exercise

numbers=list(range(1,11))

def func(numbers):
    even=[]
    odd=[]
    total=[]
    for i in numbers:
        if int(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
        
    total.append(odd) 
     
    total.append(even)
     
    return total
 
print(func(numbers))
       
print(max(func(numbers)[1]))
print(min(func(numbers)[1]))


#List unpacking
guiterists=["Michael","Jordan","Stuart"]
g1,g2,g3=guiterists
print(g1)
print(g2)
print(g3)