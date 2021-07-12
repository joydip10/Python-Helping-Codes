#
#
# STRING SLICING
#
#

language="python"

#positive indexing
#p=0
#y=1
#t=2
#h=3
#o=4
#n=5

#negative indexing (total length-positive indexing)
#p=-6
#y=-5
#t=-4
#h=-3
#o=-2
#n=-1


print(language[2])
print(language[-4]) 

#slicing string_name[start_argument:stop_argument-1:step_argument]

print("JOYOUS"[0:4:2]) 
print("JOYOUS"[0::2])
print("JOYOUS"[-1::-1])
print("JOYOUS"[::-1])


#exercise
#name=input("Enter User Name: ")
#print(f"Reversely written as: {name[::-1]}")



#
#
#STRING METHODS PART-ONE---> 
# len(), lower(),upper(),title(),count()
#


print(len("JOY DIP DAS")); #prints the length
print("JOY DIP DAS".lower()); #transforms the string into lowercase
print("joy dip das".upper()); #transforms the string into uppercase
print("jOY DIP DAS".title()); #transforms the first letter into capital and others to small letter
print("JOY DIP DAS".count("D"))#Finds the count of a certain letter in the string


#Exercise
#name, char=input("Enter a name and a character: ").split(",")
#print(name.lower().count(char.lower()))





#
#
# STRIP method->lstrip(),rstrip() and strip()
#
#

print("Without Strip Method--->"+"         JOY DIP DAS          "+"..........");
print("With lstrip Method--->"+"         JOY DIP DAS          ".lstrip()+"..........");
print("With rstrip Method--->"+"         JOY DIP DAS          ".rstrip()+"..........");
print("With strip Method--->"+"         JOY DIP DAS          ".strip()+"..........");



#There is no technique to remove the spaces between the words in a string but there is a technique using replace() method

print("Replacing interwords space using replace() method--->"+"JOY DIP DAS".replace(" ",""));










#
#
# STRING METHOD PART TWO-----> replace(),find() and center() method
#
#


print("JOY DIP   DAS".replace(" ","_"))
print("JOY was there,untill Rashed came and took the place which was there!!".replace("was","is")); #replaces all was with is
print("JOY was there,untill Rashed came and took the place which was there!!".replace("was","is",1)); #replaces was with is for one time



print("is there a good way to do something which is never done before!!".find("is"))
print("is there a good way to do something which is never done before!!".find("is",1))

print("JOY".center(11,"*"))