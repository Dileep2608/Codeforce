"""def count_x(lis):
    global count
    for i in range(3,len(lis)-1):
        if lis[i-1] == lis[i]:
            count += 1
            lis.remove(lis[i])
        else:
            break
    lis.remove(lis[0])
    lis.remove(lis[1])
    lis.remove(lis[2])
    return count


def find_x(n):
    global lis,count
    for i in range(n-2):
        if lis[i] == 'x' and lis[i+1] == 'x' and lis[i+2] == 'x':
            count += 1
            answer = count_x(lis)
            break
        else:
            lis.remove(lis[i])


n = int(input())
m = input()
lis = list(m)
cout = 0
if 'xxx' not in m:
    print(0)"""

"""def count_x(a):
    global answer,lis
    answer = 0
    count  = 1
    for i in range(1,len(a)):
        if a[i-1] == a[i]:
            count += 1
            lis.remove(a[i-1])
        else:
            break
    lis.remove(lis[0])
    answer = answer+ count-2
    return answer



def func():
    global lis,answer
    for i in range(len(lis)-2):
        if string[i] != 'x':
            lis.remove(string[i])
        elif string[i] == 'x' and string[i+1] == 'x' and string[i+2] == 'x':
            answer = count_x(str(lis[i:]))
    return answer



n = int(input())
string = input()
lis = list(string)
answer = 0
if 'xxx' not in string:
    print(0)
else:
    print(func())"""

def funct(a):
    answer = 0
    count = 1
    for i in range(len(lis)-1):
        if lis[i+1]-lis[i] == 1:
            count = count+1
        else:
            if count < 3:
                    count = 1
            elif count >= 3:
                    answer = answer + count-2
                    count = 1
    if count < 3:
        count = 1
    elif count >= 3:
        answer = answer + count - 2
        count = 1
    return answer

def func():
    global li,lis
    for i in range(len(li)):
        if li[i] == 'x':
            lis.append(i)
    answer = funct(lis)
    return answer

n = int(input())
string = input()
li = list(string)
lis = []
if 'xxx' not in string:
    print(0)
else:
    answer = func()
    print(answer)


