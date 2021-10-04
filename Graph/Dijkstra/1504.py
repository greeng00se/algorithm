import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().split())
INF = int(1e9)
lst = [[INF] * 801 for _ in range(801)]
distance = []

for _ in range(e):
    a, b, c = map(int, input().split())
    lst[a][b] = c
    lst[b][a] = c

v1, v2 = map(int, input().split())

def dijkstra(s):
    global distance
    hq = []
    visited = [0] * (n + 1)
    distance = [INF] * (n + 1)
    
    heapq.heappush(hq, (0, s))
    distance[s] = 0
    
    while hq:
        dist, now = heapq.heappop(hq)
        if visited[now]:
            continue
        visited[now] = 1
        
        for i in range(1, n + 1):
            if lst[now][i] == INF:
                continue
            if distance[i] > lst[now][i] + dist:
                distance[i] = lst[now][i] + dist
                heapq.heappush(hq, (distance[i], i))
                
result1, result2 = 0, 0
dijkstra(1)
result1 += distance[v1]
result2 += distance[v2]
dijkstra(v1)
result1 += distance[v2]
result2 += distance[n]
dijkstra(v2)
result1 += distance[n]
result2 += distance[v1]

if INF <= result1 <= result2: print(-1)
else: print(min(result1, result2))




    
    
