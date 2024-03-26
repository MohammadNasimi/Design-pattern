
from abc import ABC,abstractmethod

class Car: # product
    def __init__(self) -> None:
            self._wheel = None
            self._engine = None
            self._body = None
            
    def set_wheel(self,wheel):
        self._wheel = wheel
        
    def set_engine(self,engine):
        self._engine = engine
        
    def set_body(self,body):
        self._body = body
        
    def detail(self):
        print(f'wheel :{self._wheel.size}')
        print(f'engine :{self._engine.hp}')
        print(f'body :{self._body.shape}')
        
        

class Abstractbuilder(ABC): # Abstract Builder
    
    @abstractmethod
    def get_wheel(self):
        pass
    
    @abstractmethod
    def get_engine(self):
        pass
    
    @abstractmethod
    def get_body(self):
        pass
    
class Benz(Abstractbuilder): # concrate builder 1
    
    def get_body(self):
        body = Body()
        body.shape ='suv'
        return body
    def get_engine(self):
        engine = Engine()
        engine.hp = 123
        return engine
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 20   
        return wheel 

class Bmw(Abstractbuilder): # concrate builder 2
    
    def get_body(self):
        body = Body()
        body.shape ='m2'
        return body
    def get_engine(self):
        engine = Engine()
        engine.hp = 342
        return engine
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 23   
        return wheel 
        
class Wheel: size = None
class Engine : hp = None
class Body : shape = None


class Director:
    _builder = None
    
    def set_builder(self,builder):
        self._builder = builder
        
    def construct(self):
        car = Car()
        
        body = self._builder.get_body()
        car.set_body(body)
        engine = self._builder.get_engine()
        car.set_engine(engine)
        wheel = self._builder.get_wheel()
        car.set_wheel(wheel)
        
        return car
    
def client_builder(builder):
    builders ={
        'Bmw': Bmw,
        'Benz': Benz
    }
    car = builders[builder]()
    director = Director()
    director.set_builder(car)
    result = director.construct()
    return result.detail()

client_builder('Bmw')