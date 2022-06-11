import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def solve(n, m):
    ratio = (m * 100) // n
    if ratio >= 99:
        return -1
    l, r = 1, int(1e9)
    result = 0
    while l <= r:
        mid = (l + r) // 2
        
        nm = m + mid
        nn = n + mid
        nratio = (nm * 100) // nn
        
        if nratio > ratio:
            result = mid
            r = mid - 1
        else:
            l = mid + 1
            
    return result
    
print(solve(n, m))