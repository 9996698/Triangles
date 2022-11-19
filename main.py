from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        self._area = 0
        self._perimeter = 0

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    def get_area(self):
        return self._area

    def get_perimeter(self):
        return self._perimeter


class Point:
    def __init__(self, x=None, y=None):
        self.__x = x
        self.__y = y

    def get_x(self) -> float:
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self) -> float:
        return self.__y

    def set_y(self, y):
        self.__y = y


class Triangle(Shape):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self.type = self.__qualify_type(self.__get_side(a, b), self.__get_side(b, c), self.__get_side(a, c))
        self.type_angle = self.__qualify_type_angle
        super().__init__()

    @staticmethod
    def __get_side(p1: Point, p2: Point) -> float:
        return ((p2.get_x() - p1.get_x()) ** 2 + (p2.get_y() - p1.get_y()) ** 2) ** 0.5

    def __qualify_type(self, ab: float, bc: float, ca: float) -> float:
        pass

    def __qualify_type_angle(self, ab, bc, ca):
        pass

    def calculate_perimeter(self):
        return self._a + self._b + self._c

    def calculate_area(self):
        p = self._a + self._b + self._c
        s = p/2
        s1 = 1
        args = [self._a, self._b, self._c]
        for arg in args:
            s1 *= (s - arg)
        return print((s * s1)**0.5)


if __name__ == '__main__':
    first_point = Point(1, 3)
    second_point = Point(5, 4)
    third_point = Point(7, 2)
