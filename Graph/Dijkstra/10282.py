import sys
import heapq

INF = int(1e9)
rep = int(input())

for _ in range(rep):
    n, d, c = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, w = map(int, input().split())
        adj[b].append((a, w))
    
    visited = [INF] * (n + 1)
    visited[c] = 0
    hq = []
    heapq.heappush(hq, c)
    
    while hq:
        now = heapq.heappop(hq)
        
        for nxt in adj[now]:
            node, w = nxt
            if visited[node] > visited[now] + w:
                visited[node] = visited[now] + w
                heapq.heappush(hq, node)

    count = 0
    result = 0
    for v in visited:
        if v == INF:
            continue
        count += 1
        result = max(result, v)
        
    print(count, result)
            
    