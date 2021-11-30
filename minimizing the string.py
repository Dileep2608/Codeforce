n = int(input())
s = input()
p = n-1
for i in range(n-1):
    if s[i] > s[i+1]:
        p = i
        break
print(s[:p]+s[p+1:])
