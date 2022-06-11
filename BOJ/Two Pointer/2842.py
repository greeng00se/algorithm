import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
data = [list(input().rstrip()) for _ in range(n)]
altitude_sickness = [list(map(int, input().split())) for _ in range(n)]
start = []
h = []
count = 0
for i in range(n):
    for j in range(n):
        if data[i][j] == 'P':
            start = (i, j)
        if data[i][j] == 'K':
            count += 1
        h.append(altitude_sickness[i][j])

h = list(set(h))
h.sort()

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def isout(x, y):
    return x >= n or y >= n or x < 0 or y < 0
    
def bfs(lo, hi):
    visited = [[0] * n for _ in range(n)]
    tt = count
    q = deque()
    r, c = start
    q.append((r, c))
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if isout(nr, nc): continue
            if visited[nr][nc]: continue

            if not (lo <= altitude_sickness[nr][nc] <= hi): continue

            if data[nr][nc] == 'K': tt -= 1
            visited[nr][nc] = 1
            q.append((nr, nc))
    
    if tt <= 0: return True
    else: return False
            
result = int(1e9)
low, high = 0, 0
while high < len(h):
    while True:
        flag = False
        r, c = start
        if h[low] <= altitude_sickness[r][c] <= h[high]:
            flag = bfs(h[low], h[high])
            
        if not flag: break
        result = min(result, h[high] - h[low])
        low += 1
        if low > high: break
    high += 1
    
        
print(result)
        
    