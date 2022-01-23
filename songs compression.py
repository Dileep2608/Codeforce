n, m = map(int,input().split())
#a = []
#b = []
c = []
sum_a = 0
sum_b = 0
for i in range(n):
    p, q = map(int,input().split())
    #a.append(p)
    #b.append(q)
    sum_a += p
    sum_b += q
    c.append(p-q)
if sum_a <= m:
    print(0)
elif sum_b > m:
    print(-1)
else:
    #for i in range(n):
     #   c.append(a[i]-b[i])
    dif = sum_a - m
    count = 0
    c.sort()

   # while dif > 0:
    # dif = dif - c[-1]
     #   c.remove(c[-1])
      #  count = count+1
    for i in range(n):
        if dif > 0:
            dif = dif - c[-i-1]
            count = count+1
        else:
            break
    print(count)
