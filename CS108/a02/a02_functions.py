from __future__ import division
import math

# File: a02_functions.py
# your name: 
# your email:
# 
#

# function 0: an example of funciton definition


def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x


# put your definitions for the remaining functions below

def cube(x):
    return  x**3

def slope(x1, y1, x2, y2):
    if y2-y1 ==0:
        return 0.0
    else:
        return float((y2-y1)/(x2-x1))

def cylinder_volume(diameter, length):
    return math.pi*length*((diameter/2)**2)





# write your test code for all functions below.
# for example:
print('opposite(3) =', opposite(3))
print slope(7, 2, 3, 4)
