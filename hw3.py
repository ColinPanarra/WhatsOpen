def polyarea(n,r):
    """ compute area of a regular polygon with n sides and radius r"""
    return math.sin(2*math.pi/n)*n*r*r/2

assert polyarea(4,1) == 2
assert polyarea(4,2) == 8
assert polyarea(6,1) == 1.5 sqrt(3)
assert polyarea(1000000000,1) == math.pi (about)

""" script to find area of a regular polygon """
import math

def polyarea(n,r):
    """ compute area of a regular polygon with n sides and radius r"""
    return math.sin(2*math.pi/n)*n*r*r/2

n = float(input("number of sides: "))
r = float(input("radius: "))
a = polyarea(n,r)
print("area = "+str(a))
