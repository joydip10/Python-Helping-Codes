#__method__ means magic method or dunder method

class mobile_phone:
    def __init__(self,brand,number):
        self._brand=brand  #underscore is a naming convention of special property
        self.__number=number #double underscore is a special method
    
    @staticmethod
    def call(num):
        return f"calling {num}"



sam=mobile_phone("Samsung","01988765421")
print(sam._brand)
#print(sam.call("01706359955"))
print(sam.__dict__)

print("\n\n")

sam._brand="nokia"
print(sam._brand)
print(sam.__dict__)    

#print(sam.__number)
print(sam._mobile_phone__number)
sam._mobile_phone__number="01808765431"
print(sam._mobile_phone__number)

print("\n\n")
print(sam.__dict__)


print(sam.call('010100101'))




