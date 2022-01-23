n = int(input())
s = input()
lis = []
for i in range(n-1):
    lis.append(s[i]+s[i+1])
count = 0
answer = lis[0]
li = set(lis)
for i in li:
    if lis.count(i) > count:
        count = lis.count(i)
        answer = i
print(answer)
