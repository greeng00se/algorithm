import sys

input = sys.stdin.readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))
l, r = 0, max(trees)
result = 0

def count(mid):
    result = 0
    for tree in trees:
        if tree > mid: result += tree - mid
        if result >= m: return True
    return False

while l <= r:
    mid = (l + r) // 2
    
    if count(mid):
        result = mid
        l = mid + 1
    else:
        r = mid - 1
        
print(result)