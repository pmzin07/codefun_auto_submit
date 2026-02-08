a = input()
n = 1
tich = 1

for x in range(97, 123):
    y = a.count(chr(x))
    if y > 1:
        tich = tich * y

for i in range(len(a)):
    n = n * (len(a) - i)

print(n // tich)