

def golden():
    a = round((min(w, h) + 1) / 4)
    block = 0
    if 3 <= w and h <= 100 and 1 <= k <= a:
        for i in range(1, k+1):
            block = block + 2*(w-4*(i-1)) + 2*(h-4*(i-1)) - 4
        return block


w, h, k = map(int, input().split())
b = golden()
print(b)




