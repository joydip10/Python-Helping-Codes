import re

message ="Call me 222-222-2222, if not found then call 444-444-4444"
phoneNumber= re.compile(r"\d\d\d-\d\d\d-\d\d\d")
number=phoneNumber.search(message)
print(number.group()) #group() for finding first pattern in a string

message ="Call me 222-222-2222, if not found then call 444-444-4444"
print(phoneNumber.findall(message)) #findall() for finding all patterns in a string

#Finding area and phone number group separately

phoneNumber=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
mo=phoneNumber.search(message)
print('Area Group- ')
print(mo.group(1))
print('Phone number Group- ')
print(mo.group(2))


#Finding parenthesis literally

message="Knock me at (444) 222-222"
phoneNumber=re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d')
mo=phoneNumber.search(message)
print(mo.group())

#using pipe character

message='Batman uses the Batmobile using Batlights to move like a Bat'
batRegex=re.compile(r'Bat(man|mobile|lights)')
mo=batRegex.search(message)
print(mo.group())
print(batRegex.findall(message))