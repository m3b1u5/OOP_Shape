# ДЗ: Наследование, Полиморфизм, Инкапсуляция
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self): pass


class Rectangle(Shape):
    def __init__(self, length=2, width=2):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


class Circle(Shape):
    def __init__(self, rad=1):
        self.radius = float(rad)

    def area(self):
        return self.radius ** 2 * pi


def main():
    my_rectangle = Rectangle(15, 13)
    my_circle = Circle(15)

    print(f"Rectangle area: {my_rectangle.area()}")
    print(f"Circle area: {my_circle.area():0.2f}")


if __name__ == '__main__':
    main()
