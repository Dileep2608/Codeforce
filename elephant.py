x = int(input())
if 1 <= x <= 1000000:
    a = x//5
    b = (x % 5)//4
    c = ((x % 5)-(b*4))//3
    d = ((x % 5)-(b*4)-(c*3))//2
    e = ((x % 5)-(b*4)-(c*3)-(d*2))//1
    print(a+b+c+d+e)
