import copy 


class Prototype:
    def __init__(self) -> None:
        self._objects = {}
        
    def register(self,name,obj):
        self._objects[name]=obj
        
    def unregister(self,name):
        del self._objects[name]
        
    def clone(self,name,**kwargs):
        cloned_obj = copy.deepcopy(self._objects.get(name))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj
    
    
def client_prototype(name,obj,**kwargs):
    prototype = Prototype()
    prototype.register(name,obj)
    return prototype.clone(name,**kwargs)



class Car:
    def __init__(self,name,brand,year):
        self.name = name
        self.brand = brand 
        self.year = year
        
        
car_ = Car('samand','khodro',2004)


Car_prototype = client_prototype('car1',car_)    

print(Car_prototype.__dict__)    

Car_prototype1 = client_prototype('car1',car_,brand='benz',year=2009)    

print(Car_prototype1.__dict__)    


print(id(car_.name))
print(id(Car_prototype1.name))

print(id(car_.year))
print(id(Car_prototype1.year))