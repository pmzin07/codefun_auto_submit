n = int(input())

a, b, c = 0, 1, 1

if n == 1 or n == 2:
    print(1)
else:
    
    for _ in range(n - 2):
        
        a, b, c = b, c, a + b + c
        
    print(c)