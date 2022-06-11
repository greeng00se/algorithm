import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def isout(x, y):
    return x >= n or y >= n or x < 0 or y < 0

def bfs(x, y):
    global visited
    queue = deque()
    queue.append((x, y))
    result = 1
    visited[x][y] = 1
    
    while queue:
        r, c= queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if isout(nr, nc): continue
            if visited[nr][nc]: continue
            if data[nr][nc] == 0: continue
            
            queue.append((nr, nc))
            result += 1
            visited[nr][nc] = 1
            
    return result
            
apt = []
for i in range(n):
    for j in range(n):
        if visited[i][j]: continue
        if data[i][j] == 0: continue
        apt.append(bfs(i, j))
        
print(len(apt))
apt.sort()
for i in apt:
    print(i)

