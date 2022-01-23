n = int(input())
a = list(map(int,input().split()))
max_num = max(a)
min_num = min(a)
b = a.copy()
b.remove(min_num)
b.remove(max_num)
try:
    max1_num = max(b)
    min1_num = min(b)
    max_diff = max_num - max1_num
    min_diff = min1_num - min_num
    if min_diff>max_diff:
        print(max_num - min1_num)
    else:
        print(max1_num - min_num)
except ValueError:
    print('0')
