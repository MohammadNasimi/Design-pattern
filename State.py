import abc

class Elavetor: #context
    _state = None
    
    def __init__(self,state):
        self.set_state(state)
    
    def set_state(self,state):
        self._state = state
        self._state.set_elavetor(self)
        
    def show_state(self):
        print(f'elavetor is in {self._state.__class__.__name__} Floor')
    
    def go_up(self):
        self._state.push_up_btn()
        
    def go_down(self):
        self._state.push_down_btn()
        
class Floor(abc.ABC): # abstract state
    _elavator = None
    
    def set_elavetor(self,elavator):
        self._elavator = elavator
        
    @abc.abstractmethod
    def push_down_btn(self):
        pass
        
    @abc.abstractmethod
    def push_up_btn(self):
        pass
    
    
class FirstFloor(Floor): # concrete state
    def push_down_btn(self):
        print('already in the botton floor')
        
    def push_up_btn(self):
        print('Elavetor moving upward one floor')
        self._elavator.set_state(SecondFloor())
        
class SecondFloor(Floor): # concrete state
    def push_down_btn(self):
        print('Elavetor moving down one floor')
        self._elavator.set_state(FirstFloor())

    def push_up_btn(self):
        print('already in the top floor')


e = Elavetor(FirstFloor())
e.show_state()
e.go_up()
e.show_state()
e.go_up()
e.show_state()
e.go_down()
e.show_state()