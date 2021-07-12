user_id=["ASH1601051M","ASH1601052M","ASH1601053M"]
names=["JOY DIP DAS","ROBAITH HOSSAIN","GOLAM SHAMDANI SHANTO"]
CGPA=["3.49","3.01","3.35"]

print(zip(names,user_id,CGPA))

l1=list(zip(names,user_id,CGPA))
print(l1)

print("\n\n\n")
user_id=["ASH1601051M","ASH1601052M"]
names=["JOY DIP DAS","ROBAITH HOSSAIN","GOLAM SHAMDANI SHANTO"]
l2=dict(zip(names,user_id))
print("\n\n\nAs a dictionary: ")
print(l2)
print("\n")


#unzipping/unpacking -> *operator with zip
t1,t2,t3=zip(*l1)
print(t1)
print(t2)
print(t3)


t=zip(*l1)
print(list(t))

t=zip(*l1)
print(t)



#Exercise
print("\n\n\n\nExercise:")
l1=[1,5,3,2]
l2=[2,3,4,8]
l3=[5,1,8,2]
new_l=[]
for pair in zip(l1,l2,l3):
    new_l.append(max(pair))
    
print(l1)
print(l2)
print(l3)
print(new_l)





#Exercise
print("\n\n\nExercise2: ")
def func(*args):
    average=[]
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average
        

print(func([1,2,3],[1,2,3],[1,2,3]))


average= lambda *l:[sum(pair)/len(pair) for pair in zip(*l)] 

print(average([1,2,3],[1,2,3],[1,2,3]))