a, b, c = map(int, input().split())

if a < b + c and b < a + c and c < a + b:
    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        print("RIGHT")
    elif a*a > b*b + c*c or b*b > a*a + c*c or c*c > a*a + b*b:
        print("OBTUSE")
    else:
        print("ACUTE")