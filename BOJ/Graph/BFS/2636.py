import sys 
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

cheeze = [list(map(int, input().split())) for _ in range(n)]
count = sum(map(sum, cheeze))
result = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def isout(x, y):
    return x < 0 or y < 0 or x >= n or y >= m

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    check = 0

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if isout(nr, nc):
                continue

            if visited[nr][nc]:
                continue

            if cheeze[nr][nc]:
                visited[nr][nc] = 2
                check += 1
                continue

            visited[nr][nc] = 1
            queue.append((nr, nc))

    return visited, check

while count:
    result += 1
    visited, check = bfs()
    if count - check == 0:
        print(result)
        print(count)
        break

    count -= check

    for r in range(n):
        for c in range(m):
            if visited[r][c] == 2:
                cheeze[r][c] = 0



