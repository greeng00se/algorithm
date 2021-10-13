import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

l, r = 0, n - 1
result = [data[l], data[r]]
m = int(1e10)

while l < r:
    x = data[l] + data[r]
    
    if abs(x) < m:
        result = [data[l], data[r]]
        m = abs(x)
    
    if x > 0: r -= 1
    elif x < 0: l += 1
    else: break
    
print(*result)