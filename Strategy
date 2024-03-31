import abc

class Read: # context
    def __init__(self,sentence):
        self.sentence =sentence
        self._direction = None # strategy instance
        
    def set_direction(self,direction): # set straregy
        self._direction = direction
        
    def read(self):
        self._direction.direct(self.sentence)
        
        
class Direction(abc.ABC):# interface stategy
    
    @abc.abstractmethod
    def direct(self,data):
        pass
    
class Right(Direction): # concrete stategy
    
    def direct(self,data):
        print(data[::-1])
        
        
class Left(Direction): # concrete stategy
    
    def direct(self,data):
        print(data[::1])
        

def client(strategy,sentence):
    r =Read(sentence)
    r.set_direction(strategy)
    r.read()
    
client(Left(),'hello hassan amoooooo ')
client(Right(),'hello hassan amoooooo ')
    