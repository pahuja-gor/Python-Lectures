from abc import ABC, abstractmethod
from math import pi


class Document(ABC):
    def __init__(self, iName):
        self.name = iName

    @abstractmethod
    def show(self):
        pass
        # raise NotImplementedError("Subclass must be implemented!  Can't instantiate parent class.")


class Word(Document):
    def show(self):
        return "Showing Word doc contents"


class PDF(Document):
    def show(self):
        return "Showing PDF contents"


documents = [PDF('Document1'), Word('Document2'), PDF('Document3')]

for document in documents:
    print(document.name, document.show())

print("\n\n\n")


class Shape(ABC):
    def __init__(self, iName):
        self.name = iName

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, iName, iLength):
        super().__init__(iName)
        self.length = iLength

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return self.length * 4


class Circle(Shape):
    def __init__(self, iName, iRadius):
        super().__init__(iName)
        self.radius = iRadius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return pi * 2 * self.radius


shapes = [Square("Square1", 16), Circle("CircleA", 0.25), Square("Square2", 7)]

for shape in shapes:
    print(shape.name, shape.area(), shape.perimeter())
