from abc import ABCMeta, abstractmethod
from math import pi
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimetr(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self._radius = radius
        super().__init__()

    def calculate_area(self) -> float:
        return pi * self._radius*self._radius

    def calculate_perimetr(self) -> float:
        return 2 * pi * self._radius

    def __repr__(self):
        return f'{self.__class__.__name__}({self._radius})'


class Rectangle(Shape):
    def __init__(self, width: float, length: float) -> None:
        self._width = width
        self._length = length
        super().__init__()

    def calculate_area(self) -> float:
        return self._width * self._length

    def calculate_perimetr(self) -> float:
        return self._width * 2 + self._length * 2

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._width}, {self._length})'

class Square(Rectangle):
    def __init__(self, width: float) -> None:
        super().__init__(width, width)


def sum_up_area(shapes: list[Shape]):
    for shape in shapes:
        print(shape)
        print(f'{shape.calculate_perimetr()=}')

def main():
    square = Square(5)
    circle = Circle(1)
    rectangle = Rectangle(2, 3)
    print(square.calculate_area())
    sum_up_area([square, circle, rectangle])

main()