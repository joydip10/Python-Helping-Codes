#Two problems:
#-> Negative value for price is accepted via constructor
#-> We can't change the full_specification by changing the object's _price
#-> We can also set negative value from object's _price if the first problem is solvd
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
        #self.full_specification= self.brand+" "+self.model_name+" price : "+ str(self._price)
    
    @property
    def full_specification(self):
        return self.brand+" "+self.model_name+" price : "+ str(self._price)
    
    
    #solving third problem using setter() method
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,new_price):
        self._price=max(new_price,0)      
    
    
    def make_a_call(self,phone_number):
        print(f"Calling...{phone_number}")
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    
    
phone1=Phone("Nokia","1100",1000)
print(phone1.brand)
print(phone1.model_name)
print(phone1.price)
print(phone1.full_specification)
print(phone1.__dict__)
print("\n\n\nAfter changing _price to 500\n\n")

phone1.price=500

print(phone1.brand)
print(phone1.model_name)
print(phone1.price)
print(phone1.full_specification)
print(phone1.__dict__)
print("\n\n\nAfter changing _price to -500\n\n")

phone1.price=-500

print(phone1.brand)
print(phone1.model_name)
print(phone1.price)
print(phone1.full_specification)
print(phone1.__dict__)

