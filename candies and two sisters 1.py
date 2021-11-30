t = int(input())
if 1 <= t <= 10**4:
    for i in range(t):
        n = int(input())
        a = n-1
        b = 1
        count = 0
        if 1 <= n <= 2*(10**9):
            while a > b:
                a = a-1
                b = b+1
                count = count+1
            print(count)






