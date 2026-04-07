from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area():
        pass
    
    @abstractmethod
    def perimeter():
        pass

# Concrete Classes

class Rectangle(Shape):
     
    def __init__(self,len,breadth):
        self.len=len
        self.breadth=breadth

    def area(self):
        print (2*(self.len * self.breadth))
    
    def perimeter(self):
        print(2*(self.len + self.breadth))

r= Rectangle()
r.area(10,5)
