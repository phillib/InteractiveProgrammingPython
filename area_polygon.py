import math

def area_polygon(n, s):
    """
    Finds the area of a polygon.  n = number of sides and s = length.
    """
    area = ((float(1)/float(4)) * n * s ** 2) / (math.tan(math.pi / n))
    return area

print area_polygon(7, 3)
