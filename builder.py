
from abc import ABC,abstractmethod

class Car: # product
    def __init__(self) -> None:
            self._wheel = None
            self._engine = None
            self._body = None
            
    def set_wheel(self,wheel):
        self._wheel = wheel
        
    def set_engine(self,engine):
        self.c = engine
        
    def set_body(self,body):
        self._body = body
        
    def detail(self):
        print(f'wheel :{self._wheel}')
        print(f'engine :{self._engine}')
        print(f'body :{self._body}')
        
        

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


