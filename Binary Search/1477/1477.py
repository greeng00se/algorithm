import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def check(mid):
    tmp = 0
    idx = 0
    count = 0
    for i in range(k):
        if idx < n and data[idx] == i:
            tmp = 0
            idx += 1
        if tmp >= mid:
            tmp = 0
            count += 1
        tmp += 1

    return count

l, r = 0, k
result = 0

while l <= r:
    mid = (l + r) // 2
    if check(mid) > m:
        l = mid + 1
    else:
        r = mid - 1
        result = mid

print(result)

