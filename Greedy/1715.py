import sys
import heapq

input = sys.stdin.readline

result = 0
n = int(input())
hq = []

for _ in range(n):
    heapq.heappush(hq, int(input()))
    
while hq:
    a = heapq.heappop(hq)
    if hq: b = heapq.heappop(hq)
    else: break
    result += a + b
    heapq.heappush(hq, a + b)
    
print(result)