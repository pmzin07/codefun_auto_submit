a,b,c = map(int,input().split())
if b-a == c-b:
    print (2*c-b)
else:
    print (c*c // b)