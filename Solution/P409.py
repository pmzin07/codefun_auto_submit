n = int(input())
if n < 3:
    print(0)
elif n == 3:
    print(1)
else:
    if n % 2 == 0:
        print(2 * n - 4)
    else:
        print(2 * n - 5)