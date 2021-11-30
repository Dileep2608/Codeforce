s = input()
n = len(s)
count = 0
for i in range(n):
    if s[i] == 'a':
        count = count+1
if count > n//2:
    print(n)
else:
    print(2*count-1)








            
