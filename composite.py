from abc import ABC,abstractmethod


class Being(ABC): # Abstract component
    def add(self,child):
        pass
    def remove(self,child):
        pass
    def is_composite(self):
        return False
    
    @abstractmethod
    def execute(self):
        pass
    
    
class Animal(Being): # leaf
    def __init__(self,name):
        self.name = name
        
    def execute(self):
        return f"animal {self.name}"
    
class Human(Being): # concrete composite
    def __init__(self):
        self._childern = []
    
    def add(self,child):
        self._childern.append(child)
    def remove(self,child):
        self._childern.remove(child)
    def is_composite(self):
        return True
    
    def execute(self):
        print(f"Human composite")

        for child in self._childern:
            child.execute()
        return f"Human composite"
    
    
    
class Male(Human): # leaf
    def __init__(self,name):
        self.name = name
        
    def is_composite(self):
        return False
            
    def execute(self):
        print(f"\tHuman Male {self.name}")
    
class Female(Human): # leaf
    def __init__(self,name):
        self.name = name
        
    def is_composite(self):
        return False
            
    def execute(self):
        print(f"\tHuman Female {self.name}")
    
    
def client_composite():
    f1 = Female('mahtab')
    m1 = Male('hassan')
    m2 = Male('mmad')
    
    h1 = Human()
    h1.add(f1)
    h1.add(m1)
    h1.add(m2)
    
    h1.execute()
    
    
client_composite()