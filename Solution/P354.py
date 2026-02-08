a,b,c=map(int,input().split())
if b**2-4*a*c > 0:
    print ("2")
elif b**2-4*a*c == 0:
    print ("1")
else:
    print ("0")