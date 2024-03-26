
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
        
        

class Abstractbuilder(ABC):
    
    @abstractmethod
    def get_wheel(self):
        pass
    
    @abstractmethod
    def get_engine(self):
        pass
    
    @abstractmethod
    def get_body(self):
        pass