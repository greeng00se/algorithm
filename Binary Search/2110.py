import sys
from bisect import bisect_left

input = sys.stdin.readline

n, c = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.sort()
result = 0
s, e = 1, data[-1]

while True:
    l, r = 0, n - 1
    mid = (s + e) // 2
    count = 0
    while l <= r:
        l = bisect_left(data, data[l] + mid)
        count += 1
        
    if count >= c:  s = mid + 1
    else:  e = mid - 1
        
    if e == mid:
        result = mid
        break 

print(result)
