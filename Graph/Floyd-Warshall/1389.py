import sys

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b: graph[a][b] = 0
		
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
	
result = 0
k = int(1e9)
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF:
            tmp += graph[i][j]
    if k > tmp:
        result = i
        k = tmp
        
print(result)
    