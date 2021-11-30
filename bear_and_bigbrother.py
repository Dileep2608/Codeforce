a, b = map(int, input().split())
c = 0
if 1 <= a <= b <= 100:
    while a <= b:
        a = a*3
        b = b*2
        c = c+1
    print(c)