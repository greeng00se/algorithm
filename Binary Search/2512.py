import sys

input = sys.stdin.readline

n = int(input())
data = sorted(list(map(int, input().split())))
m = int(input())
answer = 0
def check(x):
    return sum(x if x < i else i for i in data)
        
l, r = m // n, max(data)
while l <= r:
    mid = (l + r) // 2

    if check(mid) > m:
        r = mid - 1
    else:
        l = mid + 1
        answer = max(answer, mid)
        
print(answer)
    



