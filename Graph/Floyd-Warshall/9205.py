import sys

input = sys.stdin.readline

INF = int(1e9)
rep = int(input())

for _ in range(rep):
    n = int(input()) + 2
    coord = []
    for i in range(n):
        a, b = map(int, input().split())
        coord.append((a, b))    
    
    graph = [[INF] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            xa, ya = coord[a]
            xb, yb = coord[b]
            ab = abs(xa - xb) + abs(ya - yb)
            if ab > 1000: continue
            graph[a][b] = ab   
            
    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    if 0 <= graph[0][n - 1] < INF: print('happy')
    else: print('sad')