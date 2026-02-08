import math
xo, yo, xm, ym, r = map(float, input().split())
d = math.sqrt((xo - xm)**2 + (yo - ym)**2)
if d <= r:
    print("YES")
else:
    print("NO")