import sys

input = sys.stdin.readline

INF = int(1e9)

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
for a in range(n):
    for b in range(n):
        if not graph[a][b]: graph[a][b] = INF
		
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
	
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end = ' ')
        else:
            print(1, end = ' ')
    print()
    