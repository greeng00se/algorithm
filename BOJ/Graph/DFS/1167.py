import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(101010)]
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(1, len(data) - 1, 2):
        adj[data[0]].append((data[j], data[j + 1]))
        
def bfs(x):
    visited = [int(1e9)] * 101010
    visited[x] = 0
    queue = deque()
    queue.append((x, 0))
    result = 0
    while queue:
        now, v = queue.popleft()
        
        for node in adj[now]:
            nxt, w = node
            
            if visited[nxt] > v + w:
                visited[nxt] = v + w
                queue.append((nxt, v + w))
    
    mv = 0
    for i in range(101010):
        if visited[i] == int(1e9): continue
        if visited[i] > mv:
            mv = visited[i]
            result = i
            
    return result, mv

nxt, mv = bfs(1)
nxt, mv = bfs(nxt)

print(mv)
    
    