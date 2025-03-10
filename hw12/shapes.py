# Shapes
# =========================================================
# 
# Define a shape object.  This object has abstract (empty) 
# methods for calculating the area and perimeter of the 
# shape.
#
# After that, create classes for Rectangles, Squares, 
# and Circles.
# 
# When done, the code should work like this.
#     >>> r = Rect(3,4)
#     >>> print r.area()
#     12
#     >>> sq = Square(5)
#     >>> print sq.perimeter()
#     20
#     >>> print isinstance(sq, Rectangle)
#     True
#     >>> c = Circle(3)
#     >>> print c.area()
#     28.274333882308138
#     

import math

class Shape(object):

    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

class Rect(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        self.area = self.width*self.height
        return self.area
    
    def perimeter(self):
        self.perimeter = (self.width*2) + (self.height*2)
        return self.perimeter

class Square(Rect):
    
    def __init__(self, side):
        self.width = side
        self.height = side

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        self.area = math.pi*self.radius**2
        return self.area
    
    def perimeter(self):
        self.perimeter = 2*math.pi*self.radius
        return self.perimeter




# Advanced Section
# ---------------------------------------------------------
# Add one more shape type: a polygon.  Polygons are created
# from a list of at least 3 points.
#
# >>> Polygon((0,0), (3,4), (0,4))
# >>> Polygon((0,0), (2,0), (2,2), (0,2))
#
# Perimeter should be easy to calculate, for area, use 
# method 1 on this site for finding the area of an irregular 
# polygon:
#   http://www.mathopenref.com/polygonirregulararea.html
# 
# You can find the area of a triangle with Heron's formula:
#   http://www.mathopenref.com/heronsformula.html
