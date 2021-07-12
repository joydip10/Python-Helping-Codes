class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
        
    def make_a_call(self,phone_number):
        print(f"Calling...{phone_number}")
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    

class smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        #two ways
        #Phone.__init__(self,brand,model_name,price)  ###uncommon way (used less)
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

    

phone1=Phone("Nokia","1100",1000)
one=smartphone("One plus","5",30000,"6 gb","64 gb", "20 mp")


print(phone1.full_name())
print(one.full_name())




#Multilevel inheritance

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
        
    def make_a_call(self,phone_number):
        print(f"Calling...{phone_number}")
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    

class smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        #two ways
        #Phone.__init__(self,brand,model_name,price)  ###uncommon way (used less)
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

class flagshipphone(smartphone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera=front_camera
        

phone1=Phone("Nokia","1100",1000)
one=smartphone("One plus","5",30000,"6 gb","64 gb", "20 mp")
oneplus=flagshipphone("One plus","5",30000,"6 gb","64 gb", "20 mp","16mp")
print(oneplus.full_name())

print(help(flagshipphone)) # Its method resolution order or MRO

#isinstance()


print(isinstance(oneplus,smartphone))


#issubclass


print(issubclass(flagshipphone,Phone))



















































