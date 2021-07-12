name="JOY DIP DAS"

i=0;
while(i<10):
    i=i+1;
    print(i);
    print("\n");
    
#Sum of numbers from 1 to 10:
    
sum=0;
i=0;
while(i!=11):
    sum=sum+i
    i=i+1
    
print(sum);  


#exercise:

num=1256
sum=0
while(num!=0):
    residue=num%10;
    num=num//10;
    sum=sum+residue
    
print(sum)

#exercise:

name="JOY DIP DAS"

i=0;
length=len(name);
while(i<length):
    j=0
    count=0
    while(j<length):
        if name[i]==name[j]:
            count=count+1
        j=j+1
    
    print(f"{name[i]}: {count}\n")
    i=i+1

sum=0
for i in range(1,11,1):
    sum=sum+i
    
print(sum)





#number guessing using loop

#num=56
#khela=True
#while khela==True:
    
#    user=input("Enter a number: ")
    
#    if(int(user)==int(num)):
#        print("you win!!!")
#        khela=False
#    elif int(user) > int(num):
#        print("Too High!!!")
#    else:
#        print("Too Low!!!")


#some important stuffs about range 

for i in range(10,0,-2):
    print(i)       
    
name="kachkola"
for i in name:
    print(i,end="    ")
    
    

    
