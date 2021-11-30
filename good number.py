n, k = map(int,input().split())
count = 0
b = set()
for i in range(k + 1):
    b.add(i)
for i in range(n):
    a = input()
    c = set()
    for i in range(len(a)):
        c.add(int(a[i]))
    if b.issubset(c) == True:
        count = count+1
print(count)
