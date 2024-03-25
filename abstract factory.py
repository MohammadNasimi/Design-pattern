"""
    Car --> BMW,Benz --> Suv,Coupe
         benz --> suv --> gla
         BMW --> suv --> x1
         benz --> coupe --> cls
         BMW -- > coupe --> m2
"""

from abc import ABC,abstractmethod

class Car(ABC): # Abstract Factory 
    @abstractmethod
    def call_suv(self):
        pass
    @abstractmethod
    def call_coupe(self):
        pass
    
class Benz(Car): # concrete Factory 
    def call_suv(self):
        return gla()
    def call_coupe(self):
        return cls()
    
class Bmw(Car): # concrete Factory 
    def call_suv(self):
        return x1()
    def call_coupe(self):
        return m2()
    
class suv(ABC): # abstract product
    @abstractmethod
    def create_suv(self):
        pass
    
class coupe(ABC): # abstract product
    @abstractmethod
    def create_coupe(self):
        pass
    
class gla(suv): # concrete product
    def create_suv(self):
        return "this is you suv benz"

class x1(suv): # concrete product
    def create_suv(self):
        return "this is you x1 Bmw"
    
class cls(coupe): # concrete product
    def create_coupe(self):
        return "this is you cls benz"
    
    
class m2(coupe): # concrete product
    def create_coupe(self):
        return "this is you m2 Bmw"
    
    
def client_suv(order): # client
    brands ={
        "Benz": Benz,
        "Bmw": Bmw
    }
    suv = brands[order]().call_suv()
    return suv.create_suv()
    
def client_coupe(order): # client
    brands ={
        "Benz": Benz,
        "Bmw": Bmw
    }
    suv = brands[order]().call_coupe()
    return suv.create_coupe()
    
    
print(client_suv("Benz"))
print(client_coupe("Bmw"))