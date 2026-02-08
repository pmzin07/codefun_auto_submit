n = int(input())
f0 = 0
f1 = 1
s = 0

for i in range(n - 1):
    fn = f0 + f1
    f0 = f1
    f1 = fn
    s += fn

print(s + 1)