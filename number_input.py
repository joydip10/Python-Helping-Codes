number1=input("Enter the first number: ")
number2=input("Enter the second number: ")
total=number1+number2
print("Addition resulted: "+total); #If number1=4,number2=4 then total=44
                                    #Because the input was taken as string
                                    


number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
total=number1+number2
print("Addition of numbers {} and {} resulted: {}".format(number1,number2,total));  #result will be in float


#adding int and float will result the output in float

number1=int(input("Enter the first number: "))
number2=float(input("Enter the second number: "))
total=number1+number2
print(f"Addition of numbers {number1} and {number2} resulted: {total}");  #result will be in float


#Exercise

num1,num2,num3=input("Enter three numbers: ").split(',')
average=(int(num1)+int(num2)+int(num3))/3;
print(f"Average of the numbers {num1},{num2} and {num3} is : {average}")