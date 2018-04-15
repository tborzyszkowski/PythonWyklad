#!/usr/bin/env python3
from math import pi
from inspect import getargspec

def flatten(_list):
    """
    Converts a list of lists into single list
    """

    for x in _list:
        if isinstance(x, list):
            for x in flatten(x):
                yield x
        else:
            yield x


class Figure():

    @classmethod
    def avaible(klass):
        """
        What figure classess are there 
        """
        
        direct_subclassess = klass.__subclasses__() 
        derivative_sublcassess = [child_klass.avaible() for child_klass in direct_subclassess]
        return list(flatten(direct_subclassess + derivative_sublcassess))

    @classmethod
    def requires(klass):
        """
        What information is required to create an instance of a figure
        """

        return getargspec(klass.__init__).args[1:]

    def area(self):
        """
        This is to be implemented as a read-only property
        """

        raise NotImplementedError()


class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return self.radius ** 2 * pi


class Rectangle(Figure):

    def __init__(self, width, height):
        self.width = width 
        self.height = height

    @property
    def area(self):
        return self.width * self.height


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)


def obtain_figure_data(figure):
    initial_properties = figure.requires()

    def obtain_property(prop):
       return int(input("What's the {}?\n".format(prop)))

    return list(map(obtain_property, initial_properties))


def serialize_figure_choice(figure_indicator):
    try:
        return {figure.__name__.lower(): figure for figure in Figure.avaible()}[figure_indicator]
    except KeyError as exception:
        raise ValueError("{} is not a valid chocie".format(figure_indicator))


def main():
    avaible_figure_names = map(lambda x: x.__name__, Figure.avaible()) 

    raw_choice = input("What we'll be calculatin'? [{}]\n".format(", ".join(avaible_figure_names)))
    normalized_chocie = raw_choice.lower()
    figure_class = serialize_figure_choice(normalized_chocie)
    figure_parameters = obtain_figure_data(figure_class) 

    figure = figure_class(*figure_parameters)

    print("The area is {}".format(figure.area))


if __name__ == "__main__":
    try:
        main()
    except ValueError as exception:
        print(exception)

