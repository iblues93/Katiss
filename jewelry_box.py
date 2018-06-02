"""
Work out the equations of the volume with the variable h. Find the first order derivative and find the roots.
The a,b,c are coefficients of the first order derivative and are used in the eqn x = -b +- root(b2 - 4ac) / 2a
"""

import math

num = int(input())

a = 12

for i in range(num):
    x,y = [int(n) for n in input().split(" ")]

    b = (4*x + 4*y)*-1
    c = x*y

    b24ac = math.sqrt(b*b - 4*a*c)

    h1 = (b*-1 + b24ac) / (2*a)
    h2 = (b*-1 - b24ac) / (2*a)

    vol1 = (x * y * h1) - (2 * h1*h1*y) - (2 * h1*h1*x) + (4 * h1*h1*h1)
    vol2 = (x * y * h2) - (2 * h2*h2*y) - (2 * h2*h2*x) + (4 * h2*h2*h2)

    vol = vol1 if vol1 > vol2 else vol2
    print("{:.11f}".format(vol))
        
