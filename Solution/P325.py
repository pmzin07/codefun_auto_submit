a = int(input())
b = list(map(int,input().split()))
v = 0
for i in range(a):
    if b[i] % 5 == 1 and b[i] % 2 == 0:
        v += b[i]
print (v)