import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

data = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def isout(x, y):
    return x < 0 or y < 0 or x >= n or y >= m

def bfs(r, c):
    result = 1
    visited[r][c] = 1
    queue = deque()
    queue.append((r, c))
    wall = set()
    
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if isout(nr, nc):
                continue
            if data[nr][nc] == 1:
                wall.add((nr, nc))
                continue
            if visited[nr][nc]:
                continue
            queue.append((nr, nc))
            visited[nr][nc] = 1
            result += 1
            
    for v in wall:
        r, c = v
        visited[r][c] += result
    return 0

for r in range(n):
    for c in range(m):
        if data[r][c]:
            visited[r][c] += 1
        if data[r][c] == 0 and not visited[r][c]:
            bfs(r, c)

for r in range(n):
    for c in range(m):
        if data[r][c] == 1:
            print(visited[r][c] % 10, end = '')
        else:
            print(0, end = '')
    print()
            