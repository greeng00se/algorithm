import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def isout(x, y):
    return x >= h or y >= w or x < 0 or y < 0

def wind(fire):
    newfire = [[1e9] * w for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    queue = deque()
    for f in fire:
        r, c = f
        visited[r][c] = 1
        newfire[r][c] = 0
        queue.append((r, c, -1))
    
    while queue:
        r, c, v = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if isout(nr, nc): continue
            if data[nr][nc] == '#': continue
            if visited[nr][nc]: continue
            
            visited[nr][nc] = 1
            newfire[nr][nc] = v + 1
            queue.append((nr, nc, v + 1))
    
    return newfire

def bfs(start, fire):
    queue = deque()
    queue.append((*start, 0))
    visited = [[int(1e9)] * w for _ in range(h)]
    visited[start[0]][start[1]] = 0
    while queue:
        r, c, v = queue.popleft()
            
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if isout(nr, nc): 
                return v + 1
            if data[nr][nc] == '#': 
                continue
            if fire[nr][nc] < v + 1:
                continue
            if visited[nr][nc] > v + 1:
                visited[nr][nc] = v + 1
                queue.append((nr, nc, v + 1))
                
    return -1
            
for _ in range(n):
    w, h = map(int, input().split())
    data = [list(input().rstrip()) for _ in range(h)]
    start = [0, 0]
    fire = set()
    for r in range(h):
        for c in range(w):
            if data[r][c] == '@': start = [r, c]
            if data[r][c] == '*': fire.add((r, c))
    
    fire = wind(fire)
    result = bfs(start, fire)
    if result == -1: print('IMPOSSIBLE')
    else: print(result)
    
    
    
    