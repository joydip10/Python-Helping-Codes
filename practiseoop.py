class car:
    discount=10.00
    def __init__(self,brand,price):
        self.brand=brand
        self.price=int(price)
        self.description=self.brand+" "+str(self.price)+" "+str(car.discount)
    @classmethod
    def from_string(cls,string):
        brand,price=string.split(',')
        return cls(brand,price)
    def offer_price(self):
        price= float(self.price)
        discount= float(car.discount)
        cut= (discount/100)*price
        offerprice=price-cut
        return offerprice
    @staticmethod
    def hello():
        print('Hello I am just a static method')
        
        
Volvo=car.from_string('VOLVO,50000')
print('Before Change')
print(Volvo.brand)
print(Volvo.price)
print(Volvo.description)
print(Volvo.__dict__)

Volvo.price=str(40000)

print('\nAfter Change')
print(Volvo.brand)
print(Volvo.price)
print(Volvo.description)
print(Volvo.__dict__)

print("\n")

print('Price-- ',Volvo.offer_price() )
print(Volvo.__dict__ )

car.discount=20
print('Price-- ',Volvo.offer_price() )
print(Volvo.__dict__ )

