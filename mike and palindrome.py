x = input()
n = len(x)
count = 0
if n%2 != 0:
    for i in range((n//2)+1):
        if x[i] != x[-i-1]:
            count = count +1
    if count == 1 or count == 0:
        print('YES')
    else:
        print('NO')
if n%2 == 0:
    for i in range(n//2):
        if x[i] != x[-i-1]:
            count = count +1
    if count == 1:
        print('YES')
    else:
        print('NO')


