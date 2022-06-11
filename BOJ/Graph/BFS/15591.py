import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, v = map(int, input().split())
    adj[a].append((b, v))
    adj[b].append((a, v))

def bfs(k, v):
    visited = [0] * (n + 1)
    queue = deque()
    queue.append((v, INF))

    while queue:
        now, usado = queue.popleft()
        if not visited[now] and usado >= k:
            visited[now] = 1
            for node in adj[now]:
                queue.append(node)

    print(visited.count(1) - 1)

for _ in range(m):
    a, b = map(int, input().split())
    bfs(a, b)
            