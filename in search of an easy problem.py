n = int(input())
b = list(map(int,input().split()))
for i in range(n):
    if b[i] == 1:
        y = 'HARD'
        break
    else:
        y = 'EASY'
print(y)
