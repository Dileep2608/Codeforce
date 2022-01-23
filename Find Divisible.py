"""
t = int(input())
for i in range(t):
    l,r = map(int,input().split())
    x = l
    for i in range(l+1, r+1):
        if i%x == 0:
            y = i
            break
    print(x,y)   """

t = int(input())
for i in range(t):
    l,r = map(int,input().split())
    x = l
    y = l*2
    print(x,y)