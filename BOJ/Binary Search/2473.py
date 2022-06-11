import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()
result = [0] * 3
m = int(1e10)
for i in range(n):
    l, r = i + 1, n - 1
    
    while l < r:
        v = data[i] + data[l] + data[r]
        if abs(m) > abs(v):
            m = v
            result = [data[i], data[l], data[r]]
            
        if v > 0: r -= 1
        elif v < 0: l += 1
        else: break
        
result.sort()
print(*result)
