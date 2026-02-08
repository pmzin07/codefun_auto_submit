a = int(input())
b = 1
c = 0
for i in range(1, a + 1):
    b = (b * i) % 1000
    c = (c + b) % 1000
    if b == 0:
        break
print(f"{c:04d}")