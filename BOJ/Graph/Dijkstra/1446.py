import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, d = map(int, input().split())
adj = [[] for _ in range(10001)]
for _ in range(n):
    a, b, w = map(int, input().split())
    if b > d: continue
    adj[a].append((b, w))

def dijkstra():
    distance = [INF] * (d + 1)
    distance[0] = 0
    hq = []
    heapq.heappush(hq, (0, 0))
    
    while hq:
        v, now = heapq.heappop(hq)

        if now >= d:
            continue

        if distance[now + 1] > v + 1:
            heapq.heappush(hq, (v + 1, now + 1))
            distance[now + 1] = v + 1
        
        if not adj[now]:
            continue

        for nxt in adj[now]:
            node, w = nxt
            if node > d: continue
            if distance[node] > v + w:
                distance[node] = v + w
                heapq.heappush(hq, (v + w, node))

    print(distance[d])

dijkstra()