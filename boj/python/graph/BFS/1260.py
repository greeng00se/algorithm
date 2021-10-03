from collections import deque

n, m, v = map(int, input().split())

g = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
    
for i in g:
    i.sort()
    
visited = [0] * (n + 1)

def dfs(x):
    visited[x] = 1
    print(x, end = ' ')
    for nx in g[x]:
        if not visited[nx]:
            dfs(nx)
    
def bfs(x):
    queue = deque()
    queue.append((x))
    visited[x] = 1
    while queue:
        x = queue.popleft()
        print(x, end = ' ')
        for nx in g[x]:
            if not visited[nx]:
                visited[nx] = 1
                queue.append((nx))
    return 0

dfs(v)
print()
visited = [0] * (n + 1)
bfs(v)
print()

