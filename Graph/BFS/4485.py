import sys
from collections import deque

input = sys.stdin.readline

def isout(x, y):
    return x >= n or y >= n or x < 0 or y < 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
count = 0
while True:
    count += 1
    n = int(input())
    if not n: break
        
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [[int(1e9)] * n for _ in range(n)]
    visited[0][0] = data[0][0]
    queue = deque()
    queue.append((0, 0, data[0][0]))
    
    while queue:
        r, c, v = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if isout(nr, nc):
                continue
            if visited[nr][nc] > v + data[nr][nc]:
                queue.append((nr, nc, v + data[nr][nc]))
                visited[nr][nc] = v + data[nr][nc]
                
    print('Problem ', count, ': ', visited[n - 1][n - 1], sep = '')
        
        
        
    
    