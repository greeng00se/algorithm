import sys
from collections import deque

input = sys.stdin.readline

rep = int(input())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def isout(x, y):
    return x >= (h + 2) or y >= (w + 2) or x < 0 or y < 0

def bfs():
    key = [[[-1] * (w + 2) for _ in range(h + 2)] for _ in range(3)]
    for k in range(3):
        queue = deque()
        r, c = run[k]
        queue.append((r, c))
        key[k][r][c] = 0
        while queue:
            r, c = queue.popleft()

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if isout(nr, nc): continue
                if data[nr][nc] == '*': continue
                if key[k][nr][nc] != -1: continue
                
                if data[nr][nc] == '#':
                    queue.append((nr, nc))
                    key[k][nr][nc] = key[k][r][c] + 1
                    continue
                queue.appendleft((nr, nc))
                key[k][nr][nc] = key[k][r][c]
                
    result = int(1e9)
    for i in range(h + 2):
        for j in range(w + 2):
            if data[i][j] == '*': continue
            count = 0
            if data[i][j] == '#': count -= 2
            for k in range(3):
                count += key[k][i][j]
            if count == -3: continue
            result = min(result, count)
            
    print(result)
    
for _ in range(rep):
    h, w = map(int, input().split())
    data = [['.'] * (w + 2) for _ in range(h + 2)]
    run = [(0, 0)]
    
    for i in range(1, h + 1):
        p = list(input().rstrip())
        for j in range(1, w + 1):
            data[i][j] = p[j - 1]
            if data[i][j] == '$':
                run.append((i, j))
    bfs()
