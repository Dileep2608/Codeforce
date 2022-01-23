def maximum_count():
    i = index
    new_index = i
    while i <= (n-2) and a[i] == a[i+1]:
        new_index = i+1
        i = i+1
    return new_index


def unimode():
    ans1 = True
    ans2 = True
    for i in range(index):
        if a[i] < a[i+1]:
            ans1 = True
        else:
            ans1 = False
            break
    new_index = maximum_count()
    for j in range(new_index,len(a)-1):
        if a[j] > a[j+1]:
            ans2 = True
        else:
            ans2 = False
            break
    answer = ans1 and ans2
    return answer


n = int(input())
a = list(map(int,input().split()))
maximum = max(a)
index = a.index(maximum)
final = unimode()
if final == True:
    print('YES')
else:
    print('NO')