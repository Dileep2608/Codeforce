t=int(input())
if 1 <= t <= 10**4:
	for i in range(t):
		a, b=map(int, input().split())
		if -1000 <= a <= 1000 and -1000 <= b <= 1000:
			print (a+b)
 
