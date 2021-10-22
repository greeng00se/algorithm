import sys
import heapq
from collections import deque

input = sys.stdin.readline
	
INF = int(1e9)

def dijkstra(s, e, sp, flag):
    global path
    distance = [INF] * n
    path = [[] for _ in range(n)]
    hq = []
    visited = [0] * n
    heapq.heappush(hq, (0, s))
    distance[s] = 0
    
    while hq:
        dist, now = heapq.heappop(hq)
        if visited[now]:
            continue
            
        visited[now] = 1
        
        for edge in adj[now]:
            node, w = edge
            if sp[now][node]: continue
            
            if distance[node] > dist + w:
                distance[node] = dist + w
                if flag:
                    path[node] = []
                    path[node].append(now)
                heapq.heappush(hq, (distance[node], node))
                continue
            
            if flag and distance[node] >= dist + w:
                distance[node] = dist + w
                path[node].append(now)
                heapq.heappush(hq, (distance[node], node))
                
    return distance[e]

while True:
    n, m = map(int, input().split())
    sp = [[0] * n for _ in range(n)]
    if n == m == 0:
        break
    s, e = map(int, input().split())
    adj = [[] for _ in range(n)]
    path = [-1] * n

    for _ in range(m):
        a, b, w = map(int, input().split())
        adj[a].append((b, w))

    sv = dijkstra(s, e, sp, 1)
    q = deque()
    q.append(e)
    v = [0] * n
    while q:
        now = q.popleft()
        for node in path[now]:
            if v[node]: continue
            v[now] = 1
            sp[node][now] = 1
            q.append(node)
    result = dijkstra(s, e, sp, 0)
    if result >= int(1e9): print(-1)
    else: print(result)
    
