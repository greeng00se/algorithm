import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
t = []

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def isout(x, y):
    return x >= n or y >= m or x < 0 or y < 0

def bfs(r, c, v):
    global visited

    visited[r][c] = 1
    data[r][c] = v
    queue = deque()
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if isout(nr, nc) or visited[nr][nc]:
                continue
            if data[nr][nc] == 0:
                t.append((r, c))
                continue

            data[nr][nc] = v
            visited[nr][nc] = 1
            queue.append((nr, nc))

visited = [[0] * m for _ in range(n)]
v = 0
for r in range(n):
    for c in range(m):
        if data[r][c] == 0 or visited[r][c]:
            continue
        v += 1
        bfs(r, c, v)

queue = deque(set(t))
bridge = []
while queue:
    r, c = queue.popleft()
    flag = data[r][c]
    for i in range(4):
        nr, nc = r, c
        count = -1
        while True:
            count += 1
            nr += dr[i]
            nc += dc[i]
            if isout(nr, nc) or data[nr][nc] == flag:
                break
            if data[nr][nc] == 0:
                continue
            if data[nr][nc] != flag:
                if count < 2: break
                bridge.append((count, flag, data[nr][nc]))
                break

bridge.sort()
parent = [i for i in range(v + 1)]

def union(x, y):
    a = find(x)
    b = find(y)
    parent[a] = b
    
def find(x):
    if parent[x] == x: return x
    else: 
        parent[x] = find(parent[x])
        return parent[x]

result = 0
for kind in bridge:
    value, a, b = kind
    if find(a) == find(b):
        continue
    union(a, b)
    result += value

flag = find(1)
for i in range(1, v + 1):
    if flag != find(i):
        result = -1

print(result)
