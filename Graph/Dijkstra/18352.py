import sys
import heapq

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
adj = [[] for _ in range(n + 1)]
INF = int(1e9)
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    
def dijkstra(n, s, adj):
    result = []
    hq = []
    heapq.heappush(hq, (0, s))
    visited = [0] * (n + 1)
    distance = [INF] * (n + 1)
    distance[s] = 0
    
    while hq:
        dist, now = heapq.heappop(hq)
        if visited[now]:
            continue
            
        visited[now] = 1
        
        for edge in adj[now]:
            node = edge
            
            if distance[node] > dist + 1:
                distance[node] = dist + 1
                heapq.heappush(hq, (distance[node], node))
                
    for i in range(1, n + 1):
        if distance[i] == k:
            result.append(i)
    return result

result = dijkstra(n, x, adj)
if result: print(*result)
else: print(-1)