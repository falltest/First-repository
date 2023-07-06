class Ploshad:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        self.s = 0
    def prepare(self):
        return self.s
class Square(Ploshad):
    def __init__(self, a: float):
        self.a = a
    def prepare(self):
        self.s = self.a * self.a
        return super().prepare()
class Rectangle(Ploshad):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    def prepare(self):
        self.s = self.a * self.b
        return super().prepare()

class Circle:
    def __init__(self, r):
        self.r = r
    def prepare(self):
        return 3.14 * self.r * self.r

def main():
    square = Square(4)
    rectangle = Rectangle(4, 3)
    circle = Circle(2)
    print(square.prepare())
    print(rectangle.prepare())
    print(circle.prepare())
if __name__ == '__main__':
    main()