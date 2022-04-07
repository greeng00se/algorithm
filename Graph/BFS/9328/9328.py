import sys
from collections import deque

input = sys.stdin.readline

rep = int(input())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
h, w = 0, 0

def isout(x, y):
    return x < 0 or x >= h + 2 or y < 0 or y >= w + 2

def remove(d, key):
    for r in range(h + 2):
        for c in range(w + 2):
            if d[r][c].isupper() and d[r][c].lower() == key:
                d[r][c] = '.'

for _ in range(rep):
    h, w = map(int, input().split())
    data = [['.'] * (w + 2) for _ in range(h + 2)]
    for i in range(h):
        d = list(input())
        for j in range(w):
            data[i + 1][j + 1] = d[j]

    print(*data, sep='\n')

    keys = list(input().rstrip())
    for r in range(h + 2):
        for c in range(w + 2):
            if data[r][c].isupper() and data[r][c].lower() in keys:
                data[r][c] = '.'
                
    visited = [[0] * (w + 2) for _ in range(h + 2)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    result = 0

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if isout(nr, nc):
                continue

            if data[nr][nc] == '*' or visited[nr][nc]:
                continue

            if data[nr][nc] == '.':
                queue.append((nr, nc))
                visited[nr][nc] = 1
                continue

            if data[nr][nc] == '$':
                result += 1
                queue.append((nr, nc))
                visited[nr][nc] = 1
                data[nr][nc] = '.'
                continue

            if data[nr][nc].isupper():
                continue

            if data[nr][nc].islower():
                key = data[nr][nc].lower()
                keys.append(key)
                remove(data, key)
                queue.append((nr, nc))
                data[nr][nc] = '.'
                visited = [[0] * (w + 2) for _ in range(h + 2)]
                visited[nr][nc] = 1

    print(result)