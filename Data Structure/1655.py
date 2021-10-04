import sys
import heapq

input = sys.stdin.readline

n = int(input())
l, r = [], []

for _ in range(n):
    num = int(input())
    
    if len(l) == len(r):
        heapq.heappush(l, -num)
    else:
        heapq.heappush(r, num)
        
    if r and -l[0] > r[0]:
        nl = heapq.heappop(l)
        nr = heapq.heappop(r)
        heapq.heappush(l, -nr)
        heapq.heappush(r, -nl)
        
    print(-l[0])        