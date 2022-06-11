import sys
import math

n, m = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(n)]
pool.sort()
l = 0
result = 0

for p in pool:
    a, b = p
    if l >= a: a = l + 1
    plank = math.ceil((b - a) / m)
    result += plank
    l = a + m * plank - 1
print(result)
    
    