#!/usr/bin/env python
"""
rects.py

Pygame Rectangles
=========================================================
The following section will test your knowledge of how to 
use pygame Rect, arguably pygame's best feature. Define
the following functions and test to make sure they 
work with `python run_tests.py`

Make sure to use the documentation 
http://www.pygame.org/docs/ref/rect.html


Terms:
---------------------------------------------------------
  Point:     an x,y value
               ex:  pt = 3,4

  Polygon:   a shape defined by a list of points
               ex:  poly = [ (1,2), (4,8), (0,3) ]

  Rectangle:  pygame.Rect
"""
import pygame
from pygame import Rect

# 1. poly_in_rect
#      Check to see if the polygon is completely within a given 
#      rectangle.
#
#      returns:  True or False

def poly_in_rect(poly, rect):
    "check if polygon is within rectangle"
    within = False
    for (x,y) in poly:
       if rect.collidepoint((x,y)):
           within = True
       else:
           within = False
    return within


# 2. surround_poly
#      Create a rectangle which contains the given polygon.  
#      It should return the smallest possible rectangle 
#      where poly_in_rect returns True.
#
#      returns:  pygame.Rect

RECT_SIZE = 120,300

def surround_poly(poly):
    "create a rectangle which surounds a polygon"
    xlist = []
    ylist = []
    for (x,y) in poly:
        xlist.append(x)
        ylist.append(y)
    xlist = sorted(xlist)
    ylist = sorted(ylist)

    rect1 = pygame.Rect((0,0), RECT_SIZE)    
    rect1.topleft = (xlist[0],ylist[0])
    rect1.width = xlist[-1] - xlist[0] + 1 #Needed the extra 1 to account for 0
    rect1.height = ylist[-1] - ylist[0] + 1
    return rect1
    
