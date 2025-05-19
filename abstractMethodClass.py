from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, width, height, radius):
        self.width = width
        self.height = height
        self.radius = radius

    def area(self):
        return  self.radius ** 2 
cir = Circle(2, 3, 5)
print(cir.area())  

rec = Circle(2, 3, 7)
print(rec.area())