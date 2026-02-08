import math
a, b, x, y = map(float, input().split())
if a == 0:
    print(f"{abs(y - b):.2f}")
else:
    a1 = -1 / a
    b1 = y - a1 * x
    x1 = (b - b1) / (a1 - a)
    y1 = a * x1 + b
    distance = math.sqrt((x - x1)**2 + (y - y1)**2)
    print(f"{distance:.2f}")