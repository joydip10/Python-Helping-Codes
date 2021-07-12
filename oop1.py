class Person:
    def __init__(self,name,height,weight,age):
        self.name=name
        self.height=height
        self.weight=weight
        self.age=age
        
        
joy=Person("JOY",5.1,65,23)
harsh=Person("Harsh",5.6,62,25)

#print(joy.name)
#print(harsh.name)


#Exercise------------------------------------------------>
class laptop:
    def __init__(self,brand,model,price):
        self.laptop_brand=brand
        self.laptop_model=model
        self.laptop_price=price
        

lp1=laptop("hp","Au80001",45000)
lp2=laptop("asus","asus781",36000)


print("lp1 object: ")
print("Brand",lp1.laptop_brand)
print("Model",lp1.laptop_model)
print("Price",lp1.laptop_price)


print("\n\n")

print("lp2 object: ")
print("Brand",lp2.laptop_brand)
print("Model",lp2.laptop_model)
print("Price",lp2.laptop_price)





#instance method--------------------------------------------->

class Person:
    def __init__(self,first_name,last_name,age):
        self.f_name=first_name
        self.l_name=last_name
        self.age=age
        
    def full_name(self):
        print(f"The full name of the person is {self.f_name+' '+self.l_name}\n")
    
    def is_age(self):
        return self.age>30

ob1=Person("Harsh","Vardhan",48)
ob2=Person("Jack","Benson",52)

ob1.full_name()
ob2.full_name()


if ob1.is_age()==True:
    print("Rich old man")
else:
    print("Young Old man")
    
    
#Person.full_name(ob1)
    
    
    
    

#Exercise---------------------------------------------------->
class laptop:
    def __init__(self,brand,model,price):
        self.laptop_brand=brand
        self.laptop_model=model
        self.laptop_price=price
        self.laptop_name= self.laptop_brand+' '+self.laptop_model
        
        
        
    def apply_discount(self,discount_offer):
        return self.laptop_price-(self.laptop_price*(discount_offer/100))
    
    
    
hp=laptop("hp","hpau801",50000)
print(hp.apply_discount(20))








#class variable

class Circle:
    pi=3.1416
    def __init__(self,radius):
        self.radius=radius
    
    def circumference(self):
        return Circle.pi * 2 * self.radius
    
    def area(self):
        return Circle.pi**2 * self.radius
    
    
cir1=Circle(2)
print(cir1.circumference())
print(cir1.area())






class laptop:
    discount_percent=10
    def __init__(self,brand,model,price):
        self.laptop_brand=brand
        self.laptop_model=model
        self.laptop_price=price
        self.laptop_name= self.laptop_brand+' '+self.laptop_model
        
        
        
    def apply_discount(self):
        return self.laptop_price-(self.laptop_price*(self.discount_percent/100)) #here self.discount_percent has been used instead of laptop.discount_percent




hp=laptop("asus","au8001",45000)
print(hp.discount_percent)
print(laptop.discount_percent)
print(hp.apply_discount())

laptop.discount_percent=25

print(hp.discount_percent)
print(laptop.discount_percent)
print(hp.apply_discount())



hp.discount_percent=50
print(hp.discount_percent)
print(laptop.discount_percent)
print(hp.apply_discount())
print(f"\n\n\n\n\n{hp.__dict__}")





#Exercise-------------------------------------->

class Person:
    person_instance=0
    def __init__(self):
        Person.person_instance=Person.person_instance+1
    

print(Person.person_instance)
p1=Person()
p2=Person()
p3=Person()
p4=Person()
p5=Person()
print(Person.person_instance)
print(p5.person_instance)



#Class Methods---------------------------------------------------------->

class Person:
    person_instance=0
    def __init__(self):
        Person.person_instance=Person.person_instance+1
        

    @classmethod
    def count_instance(cls):
        print(f"You have created {cls.person_instance} instance(s) of the class {cls.__name__}\n")
        
p1=Person()
p2=Person()
p3=Person()
p4=Person()
p5=Person()

Person.count_instance()



#Class method as a constructor and static methods


class Person:
    person_instance=0
    def __init__(self,name,mobile_brand):
        Person.person_instance=Person.person_instance+1
        self.name=name
        self.mobile_brand=mobile_brand

    @staticmethod
    def hello():
        return f"Hello!!"
   
    @classmethod
    def from_string(cls,string):
        a,b=string.split(',')
        return cls(a,b)

    @classmethod
    def count_instance(cls):
        print(f"You have created {cls.person_instance} instance(s) of the class {cls.__name__}\n")




p1=Person.from_string("JOY,01706359955")
p2=Person.from_string("Opu,01795489485")
p3=Person.from_string("Chandrika,01789985380")
p4=Person.from_string("Current_Office,0821717021")
p5=Person("Srabonty","01892345678")

Person.count_instance()
print(Person.hello())