import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
s, e = map(int, input().split())
m = int(input())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(s):
    q = deque()
    q.append((s, 0))
    visited = [INF] * (n + 1)
    visited[s] = 0

    while q:
        now, count = q.popleft()

        for nxt in adj[now]:
            
            if visited[nxt] != INF:
                continue
    
            visited[nxt] = count + 1
            q.append((nxt, count + 1))

    print(visited[e] if visited[e] != INF else -1)

bfs(s)