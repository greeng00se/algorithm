import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
top = max(map(max, data))
result = 0
visited = [[0] * n for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def isout(x, y):
    return x >= n or y >= n or x < 0 or y < 0

def bfs(x, y, lo):
    global visited
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if isout(nr, nc): continue
            if visited[nr][nc]: continue
            if data[nr][nc] <= lo: continue
                
            queue.append((nr, nc))
            visited[nr][nc] = 1
    
for i in range(top):
    visited = [[0] * n for _ in range(n)]
    count = 0
    for r in range(n):
        for c in range(n):
            if visited[r][c]: continue
            if data[r][c] > i:
                bfs(r, c, i)
                count += 1
    
    if count > result:
        result = count
        
print(result)
                
            