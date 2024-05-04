from abc import ABC,abstractmethod
from datetime import datetime 
from random import sample
from string import ascii_letters


class Originator:
    _state = None
    
    
    def __init__(self,state):
        self._state = state
        print(f'Originator: my state is {self._state}')
        
    def do_something(self):
        print('Orginator: I am doing something import')
        self._state = self._generetor_random_string(30)
        print(f'Orginator: state has changed to: {self._state}')

    def _generetor_random_string(self,length):
        return ''.join(sample(ascii_letters,length))
    
    def save(self):
        return ConcreteMemento(self._state)
    
    def restore(self,memento):
        self._state = memento.get_state()
        print(f'Orginator: state has changed to: {self._state}')
        

class Memento(ABC):
    @abstractmethod
    def get_name(self):
        pass
    
    def get_date(self):
        pass
    
class ConcreteMemento(Memento):
    def __init__(self,state):
        self._state = state
        self._date = str(datetime.now())
        
    def get_state(self):
        return self._state
    
    def get_name(self):
        return f'{self._date} / {self._state }'
    
    def get_date(self):
        return self._date
    
    
class CareTaker:
    def __init__(self,originator):
        self._originator = originator 
        self._mementos = []
        
    def backup(self):
        print('\ncare taker save originator state')
        self._mementos.append(self._originator.save())
        
    def undo(self):
        if not len(self._mementos):
            return None
        memento = self._mementos.pop()
        print(f'CateTaker: restoring state to : {memento.get_name()}')
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()
            
    def show_history(self):
        print('\n care taker here is list of memento:')
        for memento in self._mementos:
            print(memento.get_name())
            
            
originator = Originator('first_state')
caretaker = CareTaker(originator)
caretaker.backup()
originator.do_something()
caretaker.backup()
originator.do_something()
caretaker.backup()
originator.do_something()
caretaker.backup()
print()
caretaker.show_history()

print()

caretaker.undo()