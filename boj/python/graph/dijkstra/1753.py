import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
s = int(input())
adj = [[] for _ in range(v + 1)]
INF = int(1e9)
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    
def dijkstra(s):
    hq = []
    visited = [0] * (v + 1)
    heapq.heappush(hq, (0, s))
    distance[s] = 0
    while hq:
        dist, now = heapq.heappop(hq)
        if visited[now]:
            continue
            
        visited[now] = 1
        
        for edge in adj[now]:
            node, w = edge
            
            if distance[node] > dist + w:
                distance[node] = dist + w
                heapq.heappush(hq, (distance[node], node))
                
    for i in range(1, v + 1):
        if distance[i] >= INF: print('INF')
        else: print(distance[i])
        
dijkstra(s)
