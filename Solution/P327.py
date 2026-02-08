n = int(input())

memo = {}

def tinh(x):

    if x == n:
        return 1
    
    if x in memo:
        return memo[x]
    
    total = 0
   
    for i in range(x + 1, n + 1):
        total += tinh(i)
    
  
    memo[x] = total
    return total

print(tinh(1))