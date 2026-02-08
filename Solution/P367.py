a  =int(input())
count = 0
for i in range(a):
    if a % (i+1) == 0:
        count+=1
print(count)