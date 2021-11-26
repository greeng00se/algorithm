import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1
	
for a in range(1, n + 1):
    result = 0
    for b in range(1, n + 1):
        if graph[a][b] + graph[b][a] != 1:
            result += 1
    print(result - 1)
    
    