"""
File: check07b.py
Author: Br. Burton

Demonstrates abstract base classes.
"""

#TODO: Import anything you need for Abstract Base Classes / methods
from abc import ABC
from abc import abstractmethod

#TODO: convert this to an ABC 
class Shape(ABC):
    def __init__(self):
        self.name = ""
    
    def display(self):
        print("{} - {:.2f}".format(self.name, self.get_area()))

    #TODO: Add an abstractmethod here called get_area
    @abstractmethod
    def get_area(self):
        return 0.0

#TODO: Create a Circle class here that derives from Shape
class Circle(Shape):
    ''' Add an __init__ function, and in it, call the
        super class __init__ function, set the name variable to be
        "Circle", and the radius to be 0.0 '''
    def __init__(self, radius = 0.0):
        super().__init__()
        self.name = "Circle"
        self.radius = radius
    
    ''' Redefine the get_area() method to return
        "3.14 * radius * radius" '''
    def get_area(self):
        return 3.14 * self.radius * self.radius

#TODO: Create a Rectangle class here that derives from Shape
class Rectangle(Shape):
    ''' Add an __init__ function, and in it, call the
        super class __init__ function, set the name variable to be
        "Rectangle", and a length and width to each be 0.0. '''
    def __init__(self, width = 0.0, length = 0.0):
        super().__init__()
        self.name = "Rectangle"
        self.width = width
        self.length = length
    
    ''' Redefine the get_area() method to return "length * width" '''
    def get_area(self):
        return self.length * self.width

def main():

    #TODO: Declare your list of shapes here
    shapes = []

    command = ""

    while command != "q":
        command = input("Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")

        if command == "c":
            radius = float(input("Enter the radius: "))
            #TODO: Declare your Circle here, set its radius, and
            # add it to the list
            circle = Circle(radius)
            shapes.append(circle)
        
        elif command == "r":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            #TODO: Declare your Rectangle here, set its length
            # and width, and add it to the list
            rectangle = Rectangle(width, length)
            shapes.append(rectangle)


    # Done entering shapes, now lets print them all out:

    #TODO: Loop through each shape in the list, and call its display function
    for shape in shapes:
        shape.display()


if __name__ == "__main__":
    main()

