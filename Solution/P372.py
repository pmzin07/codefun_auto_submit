n, stt = map(int, input().split())

if n % 2 == 0:
    ssl = n // 2
else:
    ssl = (n + 1) // 2

if stt <= ssl:
    print((stt - 1) * 2 + 1)
else:
    print((stt - ssl) * 2)