import sys
import heapq

input = sys.stdin.readline

t = int(input())
hq = []
for _ in range(t):
    n = int(input())
    if n == 0:
        if not hq: print(0); continue
        n, op = heapq.heappop(hq)
        if op: print(n)
        else: print(-n)
        continue
    heapq.heappush(hq, (abs(n), n > 0))
        
        