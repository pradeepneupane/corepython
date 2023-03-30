from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 4
        self.breadth = 5

    def printarea(self):
        return self.length * self.breadth

react1 = Rectangle()
print(react1.printarea())