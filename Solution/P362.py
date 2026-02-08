a, n, mod = map(int, input().split())
x = 1
for i in range(n):
    x = (x * a) % mod
print(x)