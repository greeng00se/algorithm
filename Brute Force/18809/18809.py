import sys
from itertools import combinations 
from collections import deque

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
WATER, NO, YES, GREEN, RED, FLOWER = range(0, 5)

def isout(x, y):
    return x < 0 or y < 0 or x >= n or y >= m

def bfs(selectedLand, greenLand):
    redVisited = [[0] * m for _ in range(n)]
    greenVisited = [[0] * m for _ in range(n)]
    flower = [[0] * m for _ in range(n)]
    queue = deque()

    for r, c in selectedLand:
        if (r, c) in greenLand:
            greenVisited[r][c] = 1
            queue.append((r, c, 1, GREEN))
        else:
            redVisited[r][c] = 1
            queue.append((r, c, 1, RED))
            
    result = 0

    while queue:
        r, c, v, color = queue.popleft()

        if flower[r][c]: continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if isout(nr, nc):
                continue

            if data[nr][nc] == WATER or flower[nr][nc]:
                continue

            if (color == GREEN and redVisited[nr][nc] == v + 1) or (color == RED and greenVisited[nr][nc] == v + 1):
                flower[nr][nc] = 1
                result += 1
                continue

            if redVisited[nr][nc] or greenVisited[nr][nc]:
                continue

            queue.append((nr, nc, v + 1, color))
            if color == RED: 
                redVisited[nr][nc] = v + 1 
            else: 
                greenVisited[nr][nc] = v + 1

    return result

def solve():
    result = 0
    land = [(r, c) for r in range(n) for c in range(m) if data[r][c] == YES]

    selectedLands = list(combinations(land, green + red))
    
    for selectedLand in selectedLands:
        for greenLand in list(combinations(selectedLand, green)):
            result = max(result, bfs(selectedLand, greenLand))

    return result

n, m, green, red = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
print(solve())

