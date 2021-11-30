s = input()
n = len(s)
uc = 0
lc = 0
for i in range(n):
    if s[i].islower() == True:
        lc = lc+1
    else:
        uc = uc+1
if lc > uc or lc == uc:
    print(s.lower())
else:
    print(s.upper())


