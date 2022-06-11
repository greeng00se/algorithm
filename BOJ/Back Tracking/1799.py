import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
result = [0, 0]

black = []
white = []
for r in range(n):
    for c in range(n):
        if data[r][c] == 0: continue
        if (r + c) % 2 == 0: black.append((r, c))
        else: white.append((r, c))
            
dr = [-1, 1, 1, -1]
dc = [1, 1, -1, -1]

def isout(x, y):
    return x < 0 or y < 0 or x >= n or y >= n

def check(r, c):
    for i in range(4):
        nr, nc = r, c
        while True:
            nr = nr + dr[i]
            nc = nc + dc[i]
            if isout(nr, nc):
                break
            if visited[nr][nc]:
                return False
    return True

def dfs(color, value, cnt, flag):
    global result
    if value == len(color):
        result[flag] = max(result[flag], cnt)
        return
    
    r, c = color[value]
    if not visited[r][c] and check(r, c):
        visited[r][c] = 1
        dfs(color, value + 1, cnt + 1, flag)
        visited[r][c] = 0
    dfs(color, value + 1, cnt, flag)

dfs(white, 0, 0, 0)
dfs(black, 0, 0, 1)
print(sum(result))


        
    