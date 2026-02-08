a = int(input())
v=1
for i in range(a):
    if (i+1)%2==0:
        v*=(i+1)
print(v)