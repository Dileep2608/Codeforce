def zero_continues(zer):
    count = 0
    for i in range(zer,n):
        if lis[i] == 0:
            count = count+1
            ze.append(i)
        else:
            break
    return count

def zero():
    for i in range(n - 1):
        if i in ze:
            continue
        elif lis[i] != 0:
            if lis[i + 1] == 0:
                count = zero_continues(i + 1)
                print(i + 1, i + count + 1)
            else:
                print(i + 1, i + 1)
            ze.append(i)
        else:
            count = zero_continues(i)
            if lis[i] == 0 and lis[n-1] == 0:
                if lis[i:].count(0) == len(lis[i:])-1:
                    print(i+1,n)
                    break
                else:
                    print(i + 1, i + 1 + count)
                    ze.append(i + count)
            else:
                print(i + 1, i + 1 + count)
                ze.append(i+count)

    if lis[n - 1] != 0 and n-1 not in ze:
        print(n, n)


n = int(input())
lis = list(map(int,input().split()))
ze = []
if 0 not in lis:
    print('YES')
    print(n)
    for i in range(1, n + 1):
        print(i, i)
elif 0 in lis and lis.count(0) == n:
    print('NO')
else:
    print('YES')
    new_lis = lis.copy()
    for i in range(lis.count(0)):
        new_lis.remove(0)
    print(len(new_lis))
    zero()

