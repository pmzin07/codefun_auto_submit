a,b = map(int,input().split())
c= list(map(int,input().split()))
count = 0
for i in range(a):
    if c[i] == b:
        count +=1
print(count)