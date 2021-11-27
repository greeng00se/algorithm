import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1
                
q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    if graph[a][b] + graph[b][a] != 1: print(0)
    elif graph[a][b]: print(-1)
    else: print(1)
    