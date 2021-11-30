s = input()
t = input()
n = len(s)
m = len(t)
x = []
y = []
if n == m:
    for i in range(n):
        if s[i] in 'aeiou':
            x = x + [i]
    for i in range(m):
        if t[i] in 'aeiou':
            y = y + [i]
    if x == y:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
