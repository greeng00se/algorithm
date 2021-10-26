import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def isout(x, y):
    return x > n or y > n or x <= 0 or y <= 0

n = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    for j in range(1, n + 1):
        data[i][j] = tmp[j - 1]

def bfs(lo, hi):
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    queue = deque()
    queue.append((1, 1))
    visited[1][1] = 1
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if isout(nr, nc): continue
            if visited[nr][nc]: continue
                
            if not (lo <= data[nr][nc] <= hi): continue
            
            queue.append((nr, nc))
            visited[nr][nc] = 1
    
    if visited[n][n]: return True
    else: return False
    
result = int(1e9)
lo, hi = 0, 0
while hi <= 200:
    lo = 0
    while True:
        flag = False
        r, c = 1, 1
        if lo <= data[r][c] <= hi:
            flag = bfs(lo, hi)
            
        if not flag: break
        result = min(result, hi - lo)
        lo += 1
        if lo > hi: break
    hi += 1
    
print(result)
        
        
