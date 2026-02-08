m, n = map(int, input().split())
if n > 15 or m > 15 or n < m or m < 1 or n < 1:
    pass
else:
    s = 1
    for i in range(m, n + 1):
        s *= i
    print(s)