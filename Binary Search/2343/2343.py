import sys

input = sys.stdin.readline

def count(x, idx):
    result = 0
    for i in range(idx, n):
        result += data[i]
        if result > x:
            return i
    
    return n

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0

s, e = 1, int(1e9)

while s <= e:
    mid = (s + e) // 2
    x = 0
    idx = 0
    while x < m:
        idx = count(mid, idx)
        x += 1
              
    if idx >= n:  
        e = mid - 1
        result = mid
    else: 
        s = mid + 1

print(result)
