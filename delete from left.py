s = input()
t = input()
x = len(s)
y = len(t)
m = max(x,y)
n = min(x,y)
if x == m:
    big = s
    small = t
else:
    big = t
    small = s
if big[-1] != small[-1]:
    print(m+n)
else:
    count = 0
    """for i in range(n):
        if big[m-n+count:] != small[count:]:
            count += 1
        else:
            break
        print(m - n + count + count)"""

    for i in range(n):
        if big[-count-1] == small[-count-1]:
            count = count+1
        else:
            break
    print(m+n-count-count)