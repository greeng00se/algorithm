import sys
import heapq

input = sys.stdin.readline

v, k, e = map(int, input().split())
item = list(map(int, input().split()))
adj = [[] for _ in range(v + 1)]
INF = int(1e9)
result = 0

for _ in range(e):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    adj[b].append((a, w))
    
def dijkstra(s):
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
    
    tmp = 0
    for i in range(1, v + 1):
        if distance[i] <= k: 
            tmp += item[i - 1]
    if tmp > result:
        result = tmp
        
for i in range(1, v + 1):
    dijkstra(i)
    
print(result)

