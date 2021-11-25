import sys

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b: graph[a][b] = 0
		
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a][b] = w
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
result = INF
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        result = min(result, graph[i][j] + graph[j][i])
        
print(result if result < INF else -1)
    