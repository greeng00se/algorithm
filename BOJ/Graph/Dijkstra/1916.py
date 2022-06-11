import sys
import heapq

input = sys.stdin.readline

v = int(input())
e = int(input())
adj = [[] for _ in range(v + 1)]
INF = int(1e9)
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    
def dijkstra(s):
    global distance
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

v1, v2 = map(int, input().split())
dijkstra(v1)
print(distance[v2])
