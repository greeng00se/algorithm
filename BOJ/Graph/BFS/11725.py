import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

parent = [0] * (n + 1)
visited = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    
def bfs(x):
    queue = deque()
    queue.append((x, 1))
    
    visited[x] = 1
    
    while queue:
        x, p = queue.popleft()
        parent[x] = p
        
        for node in adj[x]:
            if visited[node]: 
                continue
            queue.append((node, x))
            visited[node] = 1        
        
bfs(1)
    
for i in range(2, n + 1):
    print(parent[i])