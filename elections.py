t = int(input())
if 1 <= t <= 10**4:
    for i in range(t):
        a, b, c = map(int, input().split())
        if c > a and c > b:
            a = c - a + 1
            b = c - b + 1
            c = 0
            print(a, b, c)
        elif b > a and b > c:
            a = b - a + 1
            c = b - c + 1
            b = 0
            print(a, b, c)
        elif a > b and a > c:
            b = a - b + 1
            c = a - c + 1
            a = 0
            print(a, b, c)
        elif a == b > c:
            c = a - c + 1
            a = 1
            b = 1
            print(a, b, c)
        elif a == c > b:
            b = a - b + 1
            a = 1
            c = 1
            print(a, b, c)
        elif b == c > a:
            a = b - a + 1
            b = 1
            c = 1
            print(a, b, c)
        elif a == b == c:
            a = 1
            b = 1
            c = 1
            print(a, b, c)


