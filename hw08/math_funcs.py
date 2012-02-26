#!/usr/bin/env python

import math

# Distance formula


def distance((a,b), (c,d)):
    dis = math.sqrt((a - c)**2 + (b - d)**2)
    print int(dis)
    return dis


#User Input

#x1 = int(raw_input("X coordinate of 1st point: "))
#y1 = int(raw_input("Y coordinates of 1st point: "))
#x2 = int(raw_input("X coordinates of 2nd point: "))
#y2 = int(raw_input("Y coordinates of 2nd point: "))


