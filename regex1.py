import re

message="Adventures of Batman"
message1="Adventures of Batmamamammanmanmanman"
message2="Adventures of Batwoman"
message3="Adventures of Batwowowowoman"

batRegex=re.compile(r'Bat(wo)?man') #? means appearances will be for 0 or 1 time
mo=batRegex.search(message)
print(mo.group())


#Area code as optional in searching the phone number
text=("Call me at 123-234-345")
text1=("Call me at 234-345")
phoneNumber=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d')
print(phoneNumber.search(text).group())


#0 or many times (*)
batRegex=re.compile(r'Bat(wo)*man') #* means appearances will be for 0 or many times
mo=batRegex.search(message3)
print(mo.group())

#0 or many times (+)
batRegex=re.compile(r'Bat(wo)+man') #+ means appearances will be for 1 or many times
mo=batRegex.search(message3)
print(mo.group())

#Repetition

repeat="HaHaHa"
repeat1="Three numbers-1234-3456-4344,2323-2323-2323,3434-4545"

repeatRegex=re.compile(r'(Ha){3}')
print(repeatRegex.search(repeat).group())

repeatRegex1=re.compile(r'((\d\d\d\d-)?\d\d\d\d-\d\d\d\d(,)?){3,}')
print(repeatRegex1.search(repeat1).group())

repeatRegex1=re.compile(r'((\d\d\d\d-)?\d\d\d\d-\d\d\d\d(,)?)')
print(repeatRegex1.findall(repeat1))

repeat2="messagemessagemessagemessagemessage"

repeatRegex=re.compile(r'(message){3,5}')
print(repeatRegex.search(repeat2).group()) #------> here {3,5} means minimum 3 and maximum 5 and {3,} means minimum 3 and maximum is infinite
repeatRegex=re.compile(r'(message){3,5}?') # non-greedy method- shortest message is calculated
print(repeatRegex.search(repeat2).group())



#allabout findall
resume='''
Numbers1: 8181-1212-2324
Numbers2: 1212-1212-1212
Numbers3: 1511-1313-1414
'''
allnumbers=re.compile(r'(\d\d\d\d)-(\d\d\d\d-\d\d\d\d)')
print(allnumbers.findall(resume)) #----> this will return list of tuples each having two elements if parenthesis is used in defining the regex that divides the regex ino two groups each phonenumber
allnumbers=re.compile(r'((\d\d\d\d)-(\d\d\d\d-\d\d\d\d))')
print(allnumbers.findall(resume)) #-----> this will return list of tuples each having three elements


#Buillding own character classes
message="Hello How are you,How are you"
messageRegex=re.compile(r'[A-Za-z ,]*')
print(messageRegex.search(message).group())
messageRegex=re.compile(r'[AEIOUaeiou B]{2}')
print(messageRegex.findall("AOeOBHBH BBUB"))

#Negative Character classes
messageRegex=re.compile(r'[^AEIOUaeiou bB]')
print(messageRegex.findall("AOeOBHBHBBUB"))


#Caret sign and dollar sign (begins with or ends with)
message="Hello! Shamim! Whats up!"
message1="Shamim! Whats up! Hello"
beginRegex=re.compile(r'^Hello')
endRegex=re.compile(r'Hello$')
print(beginRegex.search(message).group())
print(endRegex.findall(message1))

message3="1234 Hello 1234"
digitRegex=re.compile(r'^\d+ \w+ \d+$')
print(digitRegex.findall(message3))


#followed by(.)

text="I love my cat. who lives in a hat, who doesn't hurt the freindly bat, who lives in the next flat"
followedRegex=re.compile(r'.at')
print(followedRegex.findall(text))


followedRegex=re.compile(r'\w*.at')
print(followedRegex.findall(text))


followedRegex=re.compile(r'.{1,2}at') #. preceded by one or two characters of anything but it keeps the space
print(followedRegex.findall(text))


#.* 
#text="First Name: JOGA Last Name: Madha"
#followedRegex=re.compile(r':\s\w+\S')
#print(followedRegex.findall(text))

text="First Name: JOGA Last Name: Madha"
followedRegex=re.compile(r'First Name: (.*) Last Name: (.*)')
print(followedRegex.findall(text))


#*? -----------> non-greedy method

text="<to serve is to humanity> is our motto>"
followedRegex=re.compile(r'<(.*?)>') #non-greedy
print(followedRegex.findall(text))
followedRegex=re.compile(r'<(.*)>')  #greedy
print(followedRegex.findall(text))


prime="Serve all.\nProtect all.\nCare for all\n"
primeRegex=re.compile(r'(.*)',re.DOTALL)
print(primeRegex.search(prime))



#ifnorecase
vowels="AEIOUaeiou"
vowelRegex=re.compile(r'[aeiou]',re.I)
print(vowelRegex.findall(vowels))


#sub() method

subRegex=re.sub('\s', "$","Lets Enjoy The Rain")
print(subRegex)

text="AGENT ALICE AND AGENT BOB COMPLETED THE MISSION"
textRegex=re.compile(r'AGENT \w+')
print(textRegex.findall(text))
print(textRegex.sub('REDUCTED',text))

text="AGENT ALICE AND AGENT BOB COMPLETED THE MISSION"
textRegex=re.compile(r'AGENT (\w)\w*')
print(textRegex.sub(r"Agent \1****",text))   # \1 will leave the first character from substitution

#verbose mode
text='''
phone1= 0101010-0101
phone2= 0101-011-0101
phone3= 011-0111
phone4= -010-0111
'''
textRegex=re.compile(r"((\d\d\d\d)?(-)?\d\d\d-\d\d\d\d){1,}") #without verbose
l=textRegex.findall(text)
for i in l:
    print(i[0],end=" ")


textRegex=re.compile(r'''
((\d\d\d\d)?
(-)?    #comment1
\d\d\d  #comment2
-       #comment3
\d\d\d\d)#comment4
''',re.VERBOSE) #with verbose
l=textRegex.findall(text)
for i in l:
    print(i[0],end=" ")




#combination of multiple methods
    




textRegex=re.compile(r'''
((\d\d\d\d)?
(-)?    #comment1
\d\d\d  #comment2
-       #comment3
\d\d\d\d)#comment4
''',re.VERBOSE|re.I|re.DOTALL) #with verbose
l=textRegex.findall(text)
for i in l:
    print(i[0],end=" ")


print("\n")
#Email and phone
    
mails= "joyguru.jd@gmail.com, joydipNSTU@gmail.com, joydipdas@yahoo.com"
mailRegex=re.compile(r"(\w+(\W)?\w+@\w+.com)")
l=mailRegex.findall(mails)
print(l)
    

text='''
phone1= 0101010-0101
phone2= 0101-011-0101
phone3= 011-0111
phone4= -010-0111
'''
textRegex=re.compile(r"((\d\d\d\d)?(-)?\d\d\d-\d\d\d\d)") #without verbose
l=textRegex.findall(text)
for i in l:
    print(i[0],end=" ")
    
    