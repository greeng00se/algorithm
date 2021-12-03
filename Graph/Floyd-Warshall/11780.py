import sys

input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
route = [[0] * (n + 1) for _ in range(n + 1)]

def fp(a, b):
    if route[a][b] == 0:
        return []

    k = route[a][b]
    return fp(a, k) + [k] + fp(k, b)

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a][b] = min(graph[a][b], w)
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == k or a == b or k == b: continue
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                route[a][b] = k
                
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF: print(0, end = ' ')
        else: print(graph[a][b], end = ' ')
    print()
    
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF: 
            print(0)
            continue
        path = [a] + fp(a, b) + [b]
        print(len(path), *path)
    