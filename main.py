import math


class Shape:
    def __init__(self, *args):
        self.perimeter = sum(args)
        p = self.perimeter/2
        mult = 1
        for arg in args:
            mult *= (p-arg)
        self.area = (p*mult)**0.5

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter


class Point:
    def __init__(self, x=None, y=None):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y


first_point = Point(1, 3)
second_point = Point(5, 4)
third_point = Point(7, 2)
