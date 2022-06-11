import sys

input = sys.stdin.readline

while True:
    try: x = int(input())
    except: break
    x *= 10000000
    n = int(input())
    data = sorted([int(input()) for _ in range(n)])
    l, r = 0, len(data) - 1
    result = (-1, -1)
    while l < r:
        lego = data[l] + data[r]
        if lego == x:
            result = (data[l], data[r])
            break
        if lego > x:
            r -= 1
        if lego < x:
            l += 1
            
    if result == (-1, -1): print('danger')
    else: print('yes', *result)
    
    
