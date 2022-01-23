t = int(input())
for i in range(t):
    n = int(input())
    n_str = str(n)
    lis = []
    for j in range(len(n_str)):
        lis.append(n_str[j])
    sum = 0
    for j in lis:
        sum = sum + int(j)
    print(sum)