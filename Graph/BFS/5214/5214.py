import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, k, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(m)]
d = defaultdict(list)

for i in range(m):
    for station in data[i]:
        d[station].append(i)

def bfs(start):
    queue = deque()
    queue.append((start, 1))
    visited = [0] * (n + 1)
    tvisited = [0] * m
    visited[start] = 1

    while queue:
        now, dist = queue.popleft()

        if now == n: 
            return dist
        
        for i in d[now]:

            if tvisited[i]: continue
            tvisited[i] = 1

            for j in data[i]:

                if visited[j]: continue
                visited[j] = 1
                queue.append((j, dist + 1))
    
    return 0

result = bfs(1)
print(result if result else -1)
