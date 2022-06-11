import sys
import heapq

input = sys.stdin.readline

v, e, k = map(int, input().split())
adj1 = [[] for _ in range(v + 1)]
adj2 = [[] for _ in range(v + 1)]
INF = int(1e9)
result = [0] * (v + 1)

for _ in range(e):
    a, b, w = map(int, input().split())
    adj1[a].append((b, w))
    adj2[b].append((a, w))
    
def dijkstra(s, adj):
    global result
    hq = []
    heapq.heappush(hq, (0, s))
    visited = [0] * (v + 1)
    distance = [INF] * (v + 1)
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
        result[i] += distance[i]
        
dijkstra(k, adj1)
dijkstra(k, adj2)
print(max(result))
