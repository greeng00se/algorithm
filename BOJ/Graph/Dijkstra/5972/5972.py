import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, cost = map(int, input().split())
    adj[s].append((e, cost))
    adj[e].append((s, cost))

def dijkstra(s, adj):
    distance = [INF] * (n + 1)
    distance[s] = 0
    hq = []
    heapq.heappush(hq, (0, s))

    while hq:
        dist, now = heapq.heappop(hq)

        for nxt in adj[now]:
            node, cost = nxt

            if distance[node] > dist + cost:
                distance[node] = dist + cost
                heapq.heappush(hq, (distance[node], node))

    print(distance[n])

dijkstra(1, adj)




