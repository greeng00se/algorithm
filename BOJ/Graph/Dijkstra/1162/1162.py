import sys
import heapq

input = sys.stdin.readline

INF = int(1e16)

n, m, k = map(int, input().split())
adj = [[] for _ in range(n + 1)]
distance = [[INF] * (k + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    adj[b].append((a, w))

def dijkstra(startIdx):
    hq = []
    distance[startIdx][0] = 0
    heapq.heappush(hq, (0, startIdx, 0))

    while hq:
        dist, now, pack = heapq.heappop(hq)

        if distance[now][pack] < dist:
            continue

        for edge in adj[now]:
            node, w = edge

            if pack < k and distance[node][pack + 1] > dist:
                distance[node][pack + 1] = dist
                heapq.heappush(hq, (distance[node][pack + 1], node, pack + 1))    

            if distance[node][pack] > dist + w:
                distance[node][pack] = dist + w
                heapq.heappush(hq, (distance[node][pack], node, pack))

dijkstra(1)
print(min(distance[n]))
