import math

def regular_polygon_area(n, s):
    return (n * s**2) / (4 * math.tan(math.pi / n))

n = int(input())
s = float(input())
print(regular_polygon_area(n, s))