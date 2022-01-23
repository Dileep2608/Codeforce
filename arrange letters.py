def palindrome(s):
    global ans
    n = len(s)
    if n > 0:
        if s[0] == s[n-1]:
            s = s[1:n-1]
            return palindrome(s)
        else:
          ans = False
          return ans
    return ans

t = int(input())
for i in range(t):
    ans = True
    s = input()
    li = list(s)
    if palindrome(s) == False:
        print(s)
    elif li.count(li[0]) == len(li):
        print(-1)
    else:
        se = list(set(li))
        x = li.index(se[0])
        y = li.index(se[1])
        a = li[x]
        b = li[y]
        li[x] = b
        li[y] = a
        print(''.join(li))


