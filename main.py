from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        self._area = 0
        self._perimeter = 0

    @abstractmethod
    def _calculate_area(self):
        pass

    @abstractmethod
    def _calculate_perimeter(self):
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
        self.__a = a
        self.__b = b
        self.__c = c
        self.type = self.__qualify_type(self.__get_side(a, b), self.__get_side(b, c), self.__get_side(a, c))
        self.type_angle = self.__qualify_type_angle(self.__get_side(a, b), self.__get_side(b, c), self.__get_side(a, c))
        super().__init__()

    @staticmethod
    def __get_side(p1: Point, p2: Point) -> float:
        return ((p2.get_x() - p1.get_x()) ** 2 + (p2.get_y() - p1.get_y()) ** 2) ** 0.5

    def __qualify_type(self, ab: float, bc: float, ca: float) -> float:
        pass

    def __qualify_type_angle(self, ab: float, bc: float, ca: float) -> float:
        pass

    def _calculate_perimeter(self):
        return self.__a + self.__b + self.__c

    def _calculate_area(self):
        p = self.__a + self.__b + self.__c
        s = p/2
        s1 = 1
        args = [self.__a, self.__b, self.__c]
        for arg in args:
            s1 *= (s - arg)
        return (s * s1)**0.5

    def __str__(self):
        pass


if __name__ == '__main__':
    first_point = Point(1, 3)
    second_point = Point(5, 4)
    third_point = Point(7, 2)

    first_triangle = Triangle(first_point, second_point, third_point)
