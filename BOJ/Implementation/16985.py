import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline
data = [[] for _ in range(5)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(5):
    matrix = []
    for _ in range(5):
        matrix.append(list(map(int, input().split())))
    for j in range(4):
        data[i].append(matrix)
        matrix = [list(t) for t in zip(*matrix[::-1])]

def isout(x, y, z):
    return x >= 5 or y >= 5 or z >= 5 or x < 0 or y < 0 or z < 0
    
def bfs(dataOrder, spinOrder):
    global result
    dq = deque()
    if data[dataOrder[0]][spinOrder[0]][0][0] == 0:
        return
    visited = [[[int(1e9)] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 0
    dq.append((0, 0, 0))
    
    while dq:
        x, y, z = dq.popleft()
        
        if x == y == z == 4:
            if result > visited[x][y][z]:
                result = visited[x][y][z]
            return
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if isout(nx, ny, nz): continue
            if data[dataOrder[nz]][spinOrder[nz]][nx][ny] == 0: continue
            if visited[nx][ny][nz] > visited[x][y][z] + 1:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                dq.append((nx, ny, nz))

    
def spin(dataOrder, spinOrder):
    if len(spinOrder) >= 5:
        bfs(dataOrder, spinOrder)
        return
    
    for i in range(4):
        spin(dataOrder, spinOrder + [i])
        
orders = list(permutations([0, 1, 2, 3, 4], 5))
result = int(1e9)
for order in orders:
    spin(order, [])
    
print(result if result != int(1e9) else -1)



    
    


    