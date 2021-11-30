n = int(input())
count = 0
if 2 <= n <= 10**5:
    for i in range(1,n+1):
       if n%i == 0 and n-i >0:
            count=count+1
print(count)


