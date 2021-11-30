t = int(input())
count = 0
if 1 <= t <= 100:
    for i in range(t):
        x = int(input())
        if 2 <= x <= 100:
            a = x//7
            b = (x % 7)//6
            c = ((x % 7)-(b*6))//5
            d = ((x % 7)-(b*6)-(c*5))//4
            e = ((x % 7)-(b*6)-(c*5)-(d*4))//3
            f = ((x % 7)-(b*6)-(c*5)-(d*4)-(e*3))//2
            g = ((x % 7)-(b*6)-(c*5)-(d*4)-(e*3)-(f*2))//1
            print(a+b+c+d+e+f+g)


