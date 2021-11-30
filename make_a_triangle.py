a,b,c=map (int, input().split())
if 1<=a<=100 and 1<=b<=100 and 1<=c<=100:
    if a<b+c and b<a+c and  c<a+b:
        print(0)
    elif a>=b+c:
        print ((a-b-c)+1)
    elif b>=c+a:
        print ((b-a-c)+1)
    elif c>=a+b:
        print ((c-a-b)+1)
        
