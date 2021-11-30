def jump( a, b, k ) :
  if ( k % 2 == 0 ) :
    return (a - b) * k // 2
  else :
    return (a - b) *( k// 2) + a

t = int(input())
for i in range(t) :
  a, b, k = map(int, input().split())
  result = jump(a, b, k)
  print(result)