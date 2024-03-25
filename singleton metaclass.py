from typing import Any


class singleton(type):
    _instance = None 
       
    def __call__(self):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance
    

        
class car(metaclass=singleton):
    pass

a = car()
b = car()
print(id(a))
print(id(b))

