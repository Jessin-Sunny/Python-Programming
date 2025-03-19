from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, b):
        self._length = l
        self._breadth = b
    def area(self):
        return self._length * self._breadth

class Square(Shape):
    def __init__(self, s):
        self._side = s
    def area(self):
        return self._side * self._side

r = Rectangle(10, 20)
s = Square(10)
print(r.area())
print(s.area())
