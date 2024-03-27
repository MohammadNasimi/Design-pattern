

from abc import ABC,abstractmethod
import time
import datetime
class AbstractServer(ABC):
    @abstractmethod
    def recieve(self):
        pass
    
    
class Server(AbstractServer):
    def recieve(self):
        print(' request processing ....')
        time.sleep(4)
        print('Done ....')
        
    
class LogProxcy(AbstractServer):
    
    def __init__(self,server):
        self._server = server
        
    def recieve(self):
        self.loging()
        # .... another function 
        self._server.recieve()
    
    
    def loging(self):
        with open('proxcy/log.log','a') as f:
            f.write(f' logging time {datetime.datetime.now()} \n')
            
            
def client_server(server,proxcy):
    s =server()
    p = proxcy(s)
    p.recieve()
    
client_server(Server,LogProxcy)