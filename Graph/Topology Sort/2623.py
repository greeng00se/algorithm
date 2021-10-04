import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]
result = []

for _ in range(m):
    pd = list(map(int, input().split()))
    for i in range(1, len(pd) - 1):
        if i + 1 >= len(pd):
            break
        a, b = pd[i], pd[i + 1]
        if not b in adj[a]:
            adj[a].append(b)
            indegree[b] += 1
    
def topology():
    queue = deque()
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            
    while queue:
        now = queue.popleft()
        result.append(now)
        for node in adj[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                queue.append(node)
                
topology()
if len(result) < n:
    print(0)
else: 
    for i in result: print(i)
