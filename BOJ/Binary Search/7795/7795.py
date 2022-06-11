import sys

input = sys.stdin.readline

def find(v):
    l, r = 0, len(b) - 1
    rv = -1

    while l <= r:
        mid = (l + r) // 2
        if b[mid] >= v:
            r = mid - 1
        else:
            l = mid + 1
            rv = mid

    return rv

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split()))) 
    b = sorted(list(map(int, input().split())))

    result = 0
    
    for start in a:
        result += find(start) + 1
        
    print(result)