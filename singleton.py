from typing import Any


class singleton:
    _instance = None 
    def __init__(self):
        raise RuntimeError("call get_instance instead") 
    
    @classmethod
    def get_instance(cls):
        if cls.get_instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance
    
    def __new__(cls,name=None,*args, **kwargs):
        if name == "jhon":
            return None
        else:
            return super().__new__(cls,*args,**kwargs)
        
        
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print("call object singleton class")
        
a = singleton.get_instance()

b = singleton.get_instance()



print(id(a))
print(id(b))

