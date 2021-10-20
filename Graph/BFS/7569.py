import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
t = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
tc = 0
rtc = int(1e9)
result = 0
for i in range(h):
    for j in t[i]:
        tc += j.count(0)

dr = [-1, 0, 1, 0, 0, 0]
dc = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

def isout(z, y, x):
    return x >= m or y >= n or z >= h or x < 0 or y < 0 or z < 0

def bfs():
    global tc
    if tc == 0: return 0
    visited = [[[int(1e9)] * m for _ in range(n)] for _ in range(h)]
    queue = deque()
    result = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if t[i][j][k] <= 0: continue
                queue.append((i, j, k, 0))
                visited[i][j][k] = 0
                
    while queue:
        z, y, x, c = queue.popleft()
        for i in range(6):
            nz, ny, nx = z + dh[i], y + dc[i], x + dr[i]
            if isout(nz, ny, nx): continue
            if t[nz][ny][nx] == -1: continue
            if t[nz][ny][nx] == 0 and visited[nz][ny][nx] > c + 1:
                t[nz][ny][nx] = 1
                visited[nz][ny][nx] = c + 1
                queue.append((nz, ny, nx, c + 1))
                tc -= 1
    
    if tc != 0: return -1
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if visited[i][j][k] == int(1e9): continue
                result = max(result, visited[i][j][k])
    return result

print(bfs())
        
    
