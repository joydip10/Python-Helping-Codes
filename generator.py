#Generators are iterators



#generator function

def generate(a):
    for i in range(1,a+1):
        yield(i)
        
        
#generate(10)
print(generate(10))

print('\n')
for num in generate(10):
    print(num)


for num in generate(10):  #This will not generate anything since the number has been generated for one time earlier and also removed from the memory
    print(num)   
    
    
    
#Generator comprehension

print("\n\n\n\n\n\n\n")
square=(i for i in range(1,11) if(i%2==0))
for num in square:
    print(num)
    
