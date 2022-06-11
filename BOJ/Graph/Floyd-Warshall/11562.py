import sys

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, f = map(int, input().split())
    graph[a][b] = 0
    if f: graph[b][a] = 0
    else: graph[b][a] = 1

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b: graph[a][b] = 0
            
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
q = int(input())

for _ in range(q):
    a, b = map(int, input().split())
    print(graph[a][b])
        
