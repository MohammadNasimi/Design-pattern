from abc import ABC , abstractmethod


class AbstractMediator(ABC):
    @abstractmethod
    def notify(self,sender,event):
        pass
    
class ConcreteMediator(AbstractMediator):
    def __init__(self,comp_a,comp_b):
        self.com_a = comp_a
        self.com_a.set_mediator(self)
        self.com_b = comp_b
        self.com_b.set_mediator(self)

    def notify(self,sender,event):
        self.com_b.receive(event)
        
        
class AbstractComponent(ABC):
    def __init__(self,mediator=None):
        self._mediator = mediator
        
    def set_mediator(self,mediator):
        self._mediator = mediator
    @abstractmethod   
    def receive(self,event):
        pass
    @abstractmethod   
    def notify(self,event):
        pass
    
    
class Component1(AbstractComponent):
    def receive(self, event):
        print(f'Component1 received event {event}')
    def notify(self,event):
        self._mediator.notify(self,event)
    def do_a(self):
        print('Component 1 Does A.')
        self.notify('A')
        
class Component2(AbstractComponent):
    def receive(self, event):
        print(f'Component2 received event {event}')
    def notify(self,event):
        self._mediator.notify(self,event)
    def do_b(self):
        print('Component 2 Does B.')
        self.notify('B')
        
class Component3(AbstractComponent):
    def receive(self, event):
        print(f'Component3 received event {event}')
    def notify(self,event):
        self._mediator.notify(self,event)
    def do_c(self):
        print('Component 3 Does c.')
        self.notify('C')
        
        
c1 = Component1()
c2 = Component2()
c3 = Component3()


mediator = ConcreteMediator(c3,c1) # c3 sender ,c1 receive c1

c3.do_c()

mediator = ConcreteMediator(c1,c2) # c1 sender ,c1 receive c2

c1.do_a()