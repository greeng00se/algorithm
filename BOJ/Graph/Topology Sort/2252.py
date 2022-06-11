import sys
from collections import deque

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    indegree[b] += 1
    
def topology():
    queue = deque()
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            
    while queue:
        now = queue.popleft()
        print(now, end = ' ')
        for node in adj[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                queue.append(node)
                
    print()
                
topology()