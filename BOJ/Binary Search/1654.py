import sys

input = sys.stdin.readline

n, m = map(int, input().split())

wires = [int(input()) for _ in range(n)]
l, r = 1, max(wires)
answer = 0

def count(mid):
    result = 0
    for wire in wires:
        if wire >= mid:
            result += wire // mid
        if result >= m: return True
    return False

while l <= r:
    mid = (l + r) // 2
    
    if count(mid):
        answer = mid
        l = mid + 1
    else:
        r = mid - 1
        
print(answer)
