from abc import ABC,abstractmethod

class PublicVehicle(ABC): # abstract Element
    def __init__(self,dest):
        self.dest = dest 
        
    @abstractmethod
    def order_ticket(self,ordering): # accept method
        pass
    # ordering ---> visitor
    
class Train(PublicVehicle): # concrete Elemant A
    def order_ticket(self,ordering): # accept method
        ordering.train_ticket(self)
        
class Bus(PublicVehicle): # concrete Elemant B
    def order_ticket(self,ordering): # accept method
        ordering.bus_ticket(self)
    
class Plane(PublicVehicle): # concrete Elemant C
    def order_ticket(self,ordering): # accept method
        ordering.plane_ticket(self)
    
    
class Ticket(ABC):# abstract visitor
    
    @abstractmethod
    def train_ticket(self,train):
        pass
    
    @abstractmethod
    def bus_ticket(self,bus):
        pass
    
    @abstractmethod
    def plane_ticket(self,plane):
        pass
    
class Order(Ticket): # concrete visitor
    def train_ticket(self,train):
        print(f'this is a train ticket to {train.dest}')
    
    def bus_ticket(self,bus):
        print(f'this is a bus ticket to {bus.dest}')

    
    def plane_ticket(self,plane):
        print(f'this is a plane ticket to {plane.dest}')


visitor = Order()

Bus('Tehran').order_ticket(visitor)