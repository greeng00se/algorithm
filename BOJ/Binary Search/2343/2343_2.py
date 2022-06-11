import sys

input = sys.stdin.readline

def check(mid):
    x = 0
    tmp = 0
    for i in range(n):
        if tmp + data[i] > mid:
            tmp = 0
            x += 1
        tmp += data[i]

    if tmp: 
        x += 1
    
    return x <= m

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0

l, r = max(data), int(1e10)

while l <= r:
    mid = (l + r) // 2
    if check(mid):
        r = mid - 1
        result = mid
    else:
        l = mid + 1

print(result)    