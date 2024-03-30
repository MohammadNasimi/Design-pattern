from abc import ABC,abstractmethod
import random 

class AbstractPublisher(ABC):
    @abstractmethod
    def subsciber(self):
        pass
    @abstractmethod
    def unsubsciber(self):
        pass
    @abstractmethod
    def notify(self):
        pass
    
class ConcretePublisher(AbstractPublisher):
    _observers = []
    _state = None
    def subsciber(self,observer):
        self._observers.append(observer)
    def unsubsciber(self,observer):
        self._observers.remove(observer)

    def notify(self):
        print('notify subscirbe to observer')
        for observer in self._observers:
            observer.update(self)
            
    def operation(self):
        self._state = random.randrange(0,10)
        print(f'state change to : {self._state}')
        self.notify()
        
class Observer(ABC):
    @abstractmethod
    def update(self,publisher):
        pass

class ObserverA(Observer):
    def update(self,publisher):
        if publisher._state <=5:
            print(f'publisher less than 5')

class ObserverB(Observer):
    def update(self,publisher):
        if publisher._state >=5:
            print(f'publisher more than 5')

publisher = ConcretePublisher()
publisher.subsciber(ObserverA())
publisher.subsciber(ObserverB())
publisher.operation()