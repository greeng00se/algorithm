import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n + 1)  for _ in range(n + 1)]
adj = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
groups = []
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    adj[a].append(b)
    adj[b].append(a)
    
for i in range(1, n + 1):
    if visited[i]: continue
    queue = deque()
    queue.append(i)
    visited[i] = 1
    group = []
    while queue:
        now = queue.popleft()
        group.append(now)
        for nxt in adj[now]:
            if visited[nxt]: continue
            queue.append(nxt)
            visited[nxt] = 1
    group.sort()
    groups.append(group)
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
for group in groups:
    length = len(group)
    count = int(1e9)
    head = group[0]
    for i in range(length):
        tmp = 0
        for j in range(length):
            if i == j: continue
            tmp = max(tmp, graph[group[i]][group[j]])
        if tmp < count:
            head = group[i]
            count = tmp
    result.append(head)
    
print(len(result))
result.sort()
for i in result: print(i)