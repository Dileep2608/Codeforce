x = input()
n = len(x)
y = 'YES'
if x[n - 1] not in 'aeioun':
    y = 'NO'
else:
    for i in range(n - 1):
        if x[i] not in 'aeioun':
            if x[i + 1] in 'aeiou':
                y = 'YES'
            else:
                y = 'NO'
                break

print(y)

