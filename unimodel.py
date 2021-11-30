n = int(input())
s = list(map(int,input().split()))
a = 0
for i in range(n-1):
  if a == 0:
    if s[i] < s[i+1]:
      a=a+0
    else:
      a = i
  if a != 0:
    if s[i] > s[i+1]:
      a = i
    else:
      a = 0
      break
if s[-1] > s[-2]:
  a = 0
if a != 0:
  print('YES')
else:
  print('NO')