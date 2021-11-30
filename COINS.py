a, b = map(int,input().split())
count = 0
s = b
for i in range(a,0,-1):
    count = count + s//i
    s = s%i
print(count)

