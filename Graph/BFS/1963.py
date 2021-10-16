from collections import deque

rep = int(input())

MAX = 10001
er = [0] * MAX
er[0] = 1
er[1] = 1
for i in range(2, MAX):
    for j in range(i * 2, MAX, i):
        er[j] = 1

def isnotprime(x):
    return er[x]

def bfs(a, b):
    visited = [MAX] * MAX
    visited[a] = 0
    queue = deque()
    queue.append((a, 0))
    
    while queue:
        now, c = queue.popleft()
        now = str(now)
        nx = []
        for i in range(10):
            i = str(i)
            nx.append(int(i + now[1:]))
            nx.append(int(now[0] + i + now[2:]))
            nx.append(int(now[:2] + i + now[3:]))
            nx.append(int(now[:3] + i))
        
        for x in nx:
            if not 1000 <= x < 10000: continue
            if isnotprime(x): continue
            if visited[x] > c + 1:
                queue.append((x, c + 1))
                visited[x] = c + 1
        
    return visited[b]
    
    
for _ in range(rep):
    a, b = map(int, input().split())
    print(bfs(a, b))