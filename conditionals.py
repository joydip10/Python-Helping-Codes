#Exercise

import random

num=random.randint(0,100)
print(num);
user=int(input("Enter a number: "));

if(num==user):
    print("You Win!!!")
else:
    if(user>num):
        print("Bigger than the answer!");
    else:
        print("Smaller than the answer!");
        
    
    
name="Salma"
age=23
sex="F"

if (name=="kalam" and age==23) or (sex=="F"):
    print("OK!")
else:
    print("Not Ok!")


Exercise

name,age=input("Enter a name and age: ").split(",")

if (name[0]=='a' or name[0]=='A') and int(age)>10:
    print("You can watch COCO movie\n")
else:
    print("Sorry,you can not watch COCO movie\n")

#if-elif

age=60;

if age<20:
    print("Fit")
elif age>20 and age<40:
    print("Ok")
else:
    print("Should be medically checked")



#in keyword
    
    
name="JOY DIP DAS"

if "J" in name:
    print("Yes it exists")
else:
    print("No")
    
    
#check if it's empty or not
    
name="                      "

if name.strip():
    print("Not empty")
else:
    print("ëmpty")
    