from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, area=0, perimeter=0):
        self._perimeter = area
        self._area = perimeter

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

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y


if __name__ == '__main__':
    first_point = Point(1, 3)
    second_point = Point(5, 4)
    third_point = Point(7, 2)
