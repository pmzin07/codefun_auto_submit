def gt(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s
def C(k, n):
    return gt(n) // (gt(k) * gt(n - k))
a,b=map(int,input().split())
print(C(b, a))