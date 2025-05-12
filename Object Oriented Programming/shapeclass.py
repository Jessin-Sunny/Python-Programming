from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return self._width * self._height

class Triangle(Shape):
    def area(self):
        return (1/2) * self._width * self._height

r = Rectangle(10, 20)
print(r.area())
t = Triangle(10, 20)
print(t.area())

    
        
    
