x = input()
n = len(x)
Y = 'NO'
for i in range(n-6):
    if x[i] == x[i+1] == x[i+2] == x[i+3] == x[i+4] == x[i+5] == x[i+6]:
        Y = 'YES'
        break
print(Y)



