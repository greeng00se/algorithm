import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

data = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for c in range(x1, x2):
        for r in range(y1, y2):
            data[r][c] = 1

def isout(x, y):
    return x < 0 or y < 0 or x >= n or y >= m

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    rv = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if isout(nr, nc) or visited[nr][nc] or data[nr][nc]:
                continue

            queue.append((nr, nc))
            visited[nr][nc] = 1
            rv += 1

    return rv
    
result = []
for r in range(n):
    for c in range(m):
        if visited[r][c] or data[r][c]:
            continue
        count = bfs(r, c)
        result.append(count)

print(len(result))
print(*sorted(result))