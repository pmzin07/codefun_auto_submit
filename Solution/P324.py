n = int(input())
a = list(map(int, input().split()))
dem = 0
for i in range(1, n):
    if a[i-1] > a[i]:
        dem += 1
if dem == 0:
    print("YES")
else:
    print("NO")