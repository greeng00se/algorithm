import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
data = [list(map(int, input().rstrip())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def isout(x, y):
    return x >= r or y >= c or x < 0 or y < 0

def bfs(x, y):
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = 1
    
    while queue:
        r, c, w = queue.popleft()
        if r == x and c == y: return w
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if isout(nr, nc): continue
            if visited[nr][nc]: continue
            if data[nr][nc] == 0: continue
            
            queue.append((nr, nc, w + 1))
            visited[nr][nc] = 1
            
        


print(bfs(r - 1, c - 1))

