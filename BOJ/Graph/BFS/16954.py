import sys
from collections import deque

input = sys.stdin.readline

data = [list(input().rstrip()) for _ in range(8)]

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def isout(x, y):
    return x < 0 or y < 0 or x >= 8 or y >= 8

def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        visited = [[0] * 8 for _ in range(8)]

        for _ in range(len(queue)):
            r, c = queue.popleft()
            print(r, c)

            if (r, c) == (0, 7):
                return 1

            if data[r][c] == '#':
                continue

            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]

                if isout(nr, nc):
                    continue

                if visited[nr][nc]:
                    continue

                if data[nr][nc] == '#':
                    continue

                visited[nr][nc] = 1
                queue.append((nr, nc))
        
        data.pop()
        data.insert(0, [0] * 8)

    return 0

print(bfs((7, 0)))


