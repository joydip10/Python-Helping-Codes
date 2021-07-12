# Every operator's functionality is same as the other languages
#but in python division operator has two formats-
# / means float division
# // means integer division

#Here exponent operator is **

print(5/2)  # solution will be in float
print(5//2) #solution will be in integer


print(4/2) #solution will be in float such as 2.0
print(4//2) #solution will be in integer such as 2


print(2**3) #means 2^3;


#we sometimes need to round the number of digits we need in case of
#dgits comming after the decimal point-> there we can use round()

print(2**0.5) # It produces many digits after the decimal point
print(round(2**0.5,4)) #It will round the number of digits after the decimal point upto 4 places
print(round(0/3,100))


for i in range(1,11,2):
    print(i)