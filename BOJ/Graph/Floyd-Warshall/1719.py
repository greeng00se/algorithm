import sys

input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
result = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a][b] = w
    graph[b][a] = w
    result[a][b] = b
    result[b][a] = a
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b or b == k or a == k: continue
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                result[a][b] = result[a][k]
            
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if result[a][b] == INF: print('-', end = ' ')
        else: print(result[a][b], end = ' ')
    print()