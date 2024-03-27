from abc import ABC,abstractmethod


class Page(ABC): # abstract component
    @abstractmethod
    def show(self):
        pass
    
class Authpage(Page): # concrete component1 
    def show(self):
        print('page auth')
        
class NonAuthpage(Page):# concrete component2
    def show(self):
        print('anonymous page')
        
        
class PageDecorator(Page,ABC): # abstract decorator
    def __init__(self,component):
        self._component = component
        
    def show(self):
        pass
    
    
class PageAuthDecorator(PageDecorator): # Decorator
    
    def show(self):
        username = input('username:')
        password = input('pass:')
        if username == 'admin' and password == '1234':
            self._component.show()
        else:
            print('you are not authenticated')
            
            
            
def client_decorator():
    authpage = Authpage()
    authenticated = PageAuthDecorator(authpage)
    authenticated.show()
    
    
client_decorator()
    
    