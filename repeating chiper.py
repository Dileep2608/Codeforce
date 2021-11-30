n = int(input())
s = input()
v = []
count = 0
m = 1
for i in range(n):
    if i == count:
        v.append(s[i])
        count = i+m
        m = m+1
print(''.join(v))





    
    
