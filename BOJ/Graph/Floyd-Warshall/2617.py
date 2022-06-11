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
                
mid = (n + 1) // 2
result = set()

for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        count += graph[j][i]
    if count >= mid or sum(graph[i]) >= mid:
        result.add(i)
        
print(len(result))