import sys

input = sys.stdin.readline

INF = int(1e9)
n = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

while True:
    a, b = map(int, input().split())
    if a == b == -1: break
    graph[a][b] = 1
    graph[b][a] = 1
    
for i in range(1, n + 1):
    graph[i][i] = 0
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] < 2:
                continue
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                
result = [[] for _ in range(51)]
for i in range(1, n + 1):
    result[max(graph[i][1:])].append(i)
    
for i in range(51):
    if result[i]:
        print(i, len(result[i]))
        print(*result[i])
        break