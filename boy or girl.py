s = input()
n = len(s)
p = set()
for i in range(n):
    p.add(s[i])
if len(p)%2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
