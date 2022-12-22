from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        self._area = 0
        self._perimeter = 0

    @abstractmethod
    def _calculate_area(self, ab, bc, ca):
        pass

    @abstractmethod
    def _calculate_perimeter(self, ab, bc, ca):
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
        self.__type = self.__qualify_type(self.__get_side(a, b), self.__get_side(b, c), self.__get_side(c, a))
        self.__type_angle = self.__qualify_type_angle(self.__get_side(a, b), self.__get_side(b, c),
                                                      self.__get_side(c, a))
        super().__init__()

    @staticmethod
    def __get_side(p1: Point, p2: Point) -> float:
        return ((p2.get_x() - p1.get_x()) ** 2 + (p2.get_y() - p1.get_y()) ** 2) ** 0.5

    @staticmethod
    def __qualify_type(ab: float, bc: float, ca: float):
        if ab == bc == ca:
            return "equilateral"
        elif (ab == ca != bc) or (ab == bc != ca) or (bc == ca != ab):
            return "isosceles"
        elif ab != bc != ca:
            return "arbitrary"

    @staticmethod
    def __qualify_type_angle(ab: float, bc: float, ca: float):
        if round(ab ** 2, 9) == bc ** 2 + ca ** 2 or \
                round(bc ** 2, 9) == ab ** 2 + ca ** 2 or \
                round(ca ** 2, 9) == bc ** 2 + ab ** 2:
            return "right - angled"

        elif round(ab ** 2, 9) < bc ** 2 + ca ** 2 and \
                round(bc ** 2, 9) < ab ** 2 + ca ** 2 and \
                round(ca ** 2, 9) < bc ** 2 + ab ** 2:
            return "acute - angled"

        else:
            return "obtuse - angled"

    def _calculate_perimeter(self, ab, bc, ca):
        return ab + bc + ca

    def _calculate_area(self, ab: float, bc: float, ca: float):
        perimeter = ab + bc + ca
        semi_perimeter = perimeter / 2
        square = 1
        sides = [ab, bc, ca]
        for side in sides:
            square *= (semi_perimeter - side)
        return (semi_perimeter * square) ** 0.5

    def __str__(self):
        return print(f'Type of triangle: {self.__type} \
                Type of triangle of angles: {self.__type_angle} \
                Area of triangle: {self._calculate_area(self.__get_side(self.__a, self.__b), self.__get_side(self.__b, self.__c), self.__get_side(self.__c, self.__a))}\
               Perimeter of triangle: {self._calculate_perimeter(self.__get_side(self.__a, self.__b), self.__get_side(self.__b, self.__c), self.__get_side(self.__c, self.__a))}')


def main():
    return create_triangle()


def create_triangle():
    print("How many triangle do you want to create: ")
    test_cases = int(input())
    print("Input the coordinates of the points: ")
    for i in range(test_cases):
        first_point = Point(int(input()), int(input()))
        second_point = Point(int(input()), int(input()))
        third_point = Point(int(input()), int(input()))
        triangle = Triangle(first_point, second_point, third_point)
        print(triangle.__str__())


if __name__ == '__main__':
    main()
