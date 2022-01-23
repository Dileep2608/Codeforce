t = int(input())
for i in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    a = lis.count(min(lis))
    b = lis.count(max(lis))
    if a == 1:
        print((lis.index(min(lis)))+1)
    else:
        print((lis.index(max(lis)))+1)