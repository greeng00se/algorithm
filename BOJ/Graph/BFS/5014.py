from collections import deque

f, s, g, u ,d = map(int, input().split())
move = [u, -d]

def isout(x):
    return x > f or x <= 0 

def bfs():
    visited = [int(1e9)] * (f + 1)
    visited[s] = 0
    queue = deque()
    queue.append((s, 0))
    
    while queue:
        now, c = queue.popleft()
        
        for i in range(2):
            nx = now + move[i]
            if isout(nx): continue
            if visited[nx] > c + 1:
                visited[nx] = c + 1
                queue.append((nx, c + 1))
            
    if visited[g] == int(1e9): print('use the stairs')
    else: print(visited[g])
               
bfs()