import sys 
import heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())
INF = int(1e9)
adj = [[] for _ in range(1001)]
distance = [INF] * 1001

for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))

def dijkstra(s):
    hq = []
    visited = [0] * (n + 1)
    heapq.heappush(hq, (0, s))
    
    while hq:
        dist, now = heapq.heappop(hq)
        visited[now] += 1
        
        if visited[now] > k:
            continue
            
        if visited[now] == k:
            distance[now] = dist
            
        for edge in adj[now]:
            node, w = edge
            if visited[node] >= k:
                continue
            heapq.heappush(hq, (dist + w, node))
                
    for i in range(1, n + 1):
        if distance[i] >= INF: print(-1)
        else: print(distance[i])
    
dijkstra(1)