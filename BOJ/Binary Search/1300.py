import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

l, r = 0, k
result = 0

while l <= r:
    mid = (l + r) // 2
    
    count = 0
    for i in range(1, n + 1):
        count += min(n, mid // i)

    if count >= k:
        result = mid
        r = mid - 1
    else:
        l = mid + 1

print(result)