def function(n):
    rank = 1
    for i in range(n-1):
        e, f, g, h = map(int, input().split())
        if 0<=e<=100 and 0<=f<=100 and 0<=g<=100 and 0<=h<=100:
            v = e + f + g + h
        if v>t:
            rank  =rank + 1
    return rank



    
n=int(input())
a,b,c,d= map(int,input().split())
if 0<=a<=100 and 0<=b<=100 and 0<=c<=100 and 0<=d<=100:
    t=a+b+c+d
ran=function(n)
print(ran)

                                                                    

