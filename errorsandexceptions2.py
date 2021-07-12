class Animal:
    def __init__(self,name):
        self.name=name
        
    def sound(self):
        raise NotImplementedError("You haven't implemented this method in this particular subclass")  #abstract method
    
    
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
        
    def sound(self):
        return "barkings"
    

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
        
    def sound(self):
        return "meaws"
    
    
    

tommy=Dog("Tommy","Dolmesian")
print(tommy.sound())
    
