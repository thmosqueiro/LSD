# 
# Definition of the dynamical systems
# 

import numpy
from math import *


def Ex1(y,t):
    dy1 = y[0]*( 4. - y[0] ) - 2.*y[0]*y[1]
    dy2 = y[1]*( 3. - y[1] ) - y[1]*y[0]
    return [dy1,dy2]

def Pend(y, t, mu=1.2):
    dy1 = y[1]
    dy2 = -mu*sin(y[0])
    return [dy1, dy2] 

def YokoSiqueira(y, t, a = 3.0, mu=1.2):
    dy1 = y[1]
    dy2 = -mu*( y[0]**2 + y[1]**2 - a )*y[1] - y[0]
    return [dy1, dy2] 

def vanDerPol(y, t, a = 3.0, mu=1.2):
    dy1 = y[1]
    dy2 = mu*( a - y[0]**2 )*y[1] - y[0]
    return [dy1, dy2] 

