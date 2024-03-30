from abc import ABC , abstractmethod

class Command(ABC): 
    @abstractmethod
    def execute(self):
        pass
    
    
class SimpleCommand(Command): # Concrete Command
    def __init__(self,payload):
        self._payload = payload
    def execute(self):
        print(f'simple command printing {self._payload}')
        
        
class ComplexCommand(Command): # Concrete Command
    def __init__(self,reciever,a,b):
        self._reciever =reciever
        self._a = a
        self._b = b
        
    def execute(self):
        print('printing complex command and do command in reciever.',end=' ')
        self._reciever.do_something(self._a)
        self._reciever.do_something_else(self._b)
        
        
class Reciever:
    def do_something(self,a):
        print(f'\n\t reciever {a}.',end='')
    def do_something_else(self,b):
        print(f'\n\t reciever {b}.',end='')
        
        
class Invoker:
    _on_start = None
    _on_end = None
    def set_command_start(self,command):
        self._on_start = command
        
    def set_command_end(self,command):
        self._on_end = command
        
    def operation(self):
        self._on_start.execute()
        self._on_end.execute()
        
        
invoker = Invoker()
invoker.set_command_start(SimpleCommand('say hello ???'))

reciever = Reciever()

invoker.set_command_end(ComplexCommand(reciever,"save ctrl + c","copy"))


invoker.operation()