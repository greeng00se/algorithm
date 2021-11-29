import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def solve():
    remove = [[1] * n for _ in range(n)]
    result = 0
    for k in range(n):
        for a in range(n):
            for b in range(n):
                if k == a or k == b or a == b: continue
                if graph[a][b] > graph[a][k] + graph[k][b]:
                    result = -1
                if graph[a][b] == graph[a][k] + graph[k][b]:
                    remove[a][b] = 0

    if result == -1: return result
    for i in range(n):
        for j in range(i, n):
            result += graph[i][j] if remove[i][j] else 0
            
    return result

print(solve())