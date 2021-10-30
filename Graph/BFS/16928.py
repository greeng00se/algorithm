import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
move = [0] * 101

for _ in range(n + m):
    a, b = map(int, input().split())
    move[a] = b

def bfs():
    visited = [int(1e9)] * 101
    queue = deque()
    queue.append(1)
    visited[1] = 0
    
    while queue:
        now = queue.popleft()
            
        for i in range(1, 7):
            nxt = now + i
            
            if nxt >= 101: continue
            if move[nxt]:
                nxt = move[nxt]
            if visited[nxt] > visited[now] + 1:
                visited[nxt] = visited[now] + 1    
                queue.append(nxt)
                
    print(visited[100])
            
bfs()