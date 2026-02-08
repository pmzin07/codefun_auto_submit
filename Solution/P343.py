m, n = map(int, input().split())

if 1 <= m <= n <= 15:
    s = 1
    for i in range(m, n + 1):
        if i % 2 == 1:
            s *= i
    print(s)