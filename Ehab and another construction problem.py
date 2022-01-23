n = int(input())
if n == 1:
    print(-1)
else:
    b = 2
    if n % 2 == 0:
        a = n
    else:
        a = n-1
    print(a,b)            
