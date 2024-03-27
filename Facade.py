


class Cpu: # subsystem A
    def execute(self):
        print('executing data.')
        
        
class Memory: # subsystem B
    def load(self):
        print('Loading data.')
         
class SSD: # subsystem C
    def read(self):
        print('reading data.')
        
        
        
class Computer: # Facade
    def __init__(self) -> None:
        self.cpu = Cpu()
        self.ssd = SSD()
        self.memory = Memory()
        
    def start(self):
        self.memory.load()
        self.cpu.execute()
        self.ssd.read()
        
        
def client_facade():
        computer_facade = Computer()
        computer_facade.start()
        
        

client_facade()