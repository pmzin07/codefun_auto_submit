import math
a,b = map(int,input().split())
v = 0
for i in range(a):
    v= v + math.factorial(i+1)
print(v%b)