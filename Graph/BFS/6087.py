import sys
from collections import deque

INF = int(1e9)
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
data = [list(input()) for _ in range(m)]
start = []

for r in range(m):
    for c in range(n):
        if data[r][c] == 'C':
            start.append((r, c))

def isout(x, y):
    return x >= m or y >= n or x < 0 or y < 0

def bfs(start):
    queue = deque()
    r, c = start[0]
    queue.append((r, c))
    visited = [[INF] * n for _ in range(m)]
    visited[r][c] = -1
    while queue:
        r, c= queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            while True:
                if isout(nr, nc):
                    break

                if data[nr][nc] == '*':
                    break

                if visited[nr][nc] < visited[r][c] + 1:
                    break
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))
                nr += dr[i]
                nc += dc[i]
                
    r, c = start[1]
    print(visited[r][c])
    
bfs(start)
            
        
        