n = int(input())
b = list(map(int,input().split()))
count = 0
a = 0
for i in range(n):
    if a+b[i] < 0:
        count = count+1
    if a+b[i] >= 0:
        a = a+b[i]
print(count)
