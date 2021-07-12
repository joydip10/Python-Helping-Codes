class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        
    def phone_name(self):
        return f"{self.brand}  {self.model}"
    
  #from here all methods are dunder methods or special methods  they are neither instance method nor class methods they can be called without .(dot) way
    def __repr__(self):
        return f"Phone({self.brand},{self.model},{self.price})"
        
    def __str__(self):
        return f"{self.brand},{self.model},{self.price}"

    def __len__(self):
        return len(self.phone_name())
    
    def __add__(self,other):
        if isinstance(other,Phone):
            return self.price+other.price
        else:
            return self.price+other
        
        
    def __mul__(self,other):
        if isinstance(other,Phone):
            return self.price*other.price
        else:
            return self.price*other
    
# in case of lists objects, we use print(l) to print the list elements
#        but here we can't use print(phone_object)
        # to do so we can use two methods 
        # str and repr
        
p=Phone("Nokia","1100",1000)
print(p)
print(str(p))
print(p.__str__())
print(p.__repr__())
print("Length of the phone name: "+ str(len(p)))
print("Overloaded operator(+): "+str(p+p))
print("Overloaded operator(*): "+str(p*p))
print("Overloaded operator(*): "+str(p*2))

