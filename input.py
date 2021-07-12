name=input("Type your name: ");
print("Name is: "+name);

age=input("What's your age: ");
print("Age of Mr."+name+" is: "+age);


#Erroneous code
#age=int(input("What's your age: "));
#print("Age of Mr."+name+" is: "+age); #error-> because + means concatenation
                                      #here age is taken as integer and is being trying to added as string in the print() func


age=int(input("What's your age: "));
print("Age of Mr."+name+" is: "+str(age));#now we will get no error




#Multiple input in single line

name,age="JOY",23
print("Name: "+name)
print("Age: "+str(age))


name,age=input("Enter name and age: ").split()
print("Name: "+name)
print("Age: "+str(age))

name,age=input("Enter name and age: ").split(',')
print("Name: "+name)
print("Age: "+str(age))



                                      