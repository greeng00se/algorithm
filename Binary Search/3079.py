import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]

l = min(data)
result = r = max(data) * m

while l <= r:
    total = 0
    mid = (l + r) // 2
    for i in range(n):
        total += mid // data[i]
        
    if total >= m:
        r = mid - 1
        result = min(result, mid)
    else:
        l = mid + 1
        
print(result)