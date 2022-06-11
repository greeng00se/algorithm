import sys

input = sys.stdin.readline

dr = [-1, 0, 1]
dc = [1, 1, 1]

n, m = map(int, input().split())
data = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def isout(x, y):
    return x < 0 or x >= n or y < 0 or y >= m

def dfs(r, c):
    visited[r][c] = 1
        
    if c == m - 1:
        return True
        
    for i in range(3):
        nr = r + dr[i]
        nc = c + dc[i]

        if isout(nr, nc):
            continue

        if visited[nr][nc] or data[nr][nc] == 'x':
            continue

        if dfs(nr, nc):
            return True

    return False

result = 0
for i in range(n):
    if data[i][0] == '.' and dfs(i, 0):
        result += 1
    
print(result)