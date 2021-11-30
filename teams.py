n = int(input())
count = 0
for i in range(n):
    a, b, c = map(int, input().split())
    if 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1:
        if a+b+c == 2 or a+b+c == 3:
            count = count+1
print(count)