n = int(input())
s = input()
c = []
for i in range(n):
    c.append(s[i])
for i in range(n-1):
    if c[i] == 'U' and c[i+1] == 'R':
        c[i] = 'D'
        c[i+1] = 'D'
    if c[i] == 'R' and c[i+1] == 'U':
        c[i] = 'D'
        c[i+1] = 'D'
print(n-((c.count('D'))//2))
