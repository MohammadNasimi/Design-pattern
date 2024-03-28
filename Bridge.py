from abc import ABC


class Shape(ABC): # Abstraction
    def __init__(self,color):
        self.color = color
        
    def show(self):
        pass
    

class Circle(Shape): #  Refined Abstraction
    def show(self):
        self.color.paint(self.__class__.__name__)
        
class Square(Shape): #  Refined Abstraction
    def show(self):
        self.color.paint(self.__class__.__name__)
        
        
class Color(ABC): #  Abstract implemention
    def paint(self,name):
        pass 
    
class Blue(Color):# concrete implemention
    def paint(self,name):
        print(f'this is blue {name}')
        
class Red(Color): # concrete implemention
    def paint(self,name):
        print(f'this is red {name}')


r = Red()
b = Blue()
shape = Circle(r)
shape1 = Square(b)

shape.show()
shape1.show()