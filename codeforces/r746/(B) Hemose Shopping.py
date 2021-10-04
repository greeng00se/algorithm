import sys

input = sys.stdin.readline

rep = int(input())

def isgood(a):
    tmp = a[0]
    for i in a:
        if i < tmp:
            return False
        tmp = i
    return True

for _ in range(rep):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    if isgood(a):
        print('YES')
        continue
        
    arr = []
    for i in range(n):
        if i - x < 0 and i + x >= n:
            arr.append((i, a[i]))
    
    a.sort()
    flag = 1
    for node in arr:
        i, v = node
        if a[i] != v:
            flag = 0
            break
            
    if flag: print('YES')
    else: print('NO')
        
    
        