import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
MAX_VALUE = int(1e9)

flower = [(r, c) for r in range(1, n - 1) for c in range(1, n - 1)]
locations = list(combinations(flower, 3))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def check(location):
    visited = [[0] * n for _ in range(n)]
    result = 0
    for r, c in location:
        result += data[r][c]
        visited[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if visited[nr][nc]:
                return MAX_VALUE
            result += data[nr][nc]
            visited[nr][nc] = 1

    return result

result = MAX_VALUE
for location in locations:
    result = min(result, check(location))

print(result)

