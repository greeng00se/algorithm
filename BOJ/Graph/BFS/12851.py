import sys 
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 10 ** 5 + 1

def bfs():
    visited = [MAX] * MAX
    queue = deque()
    queue.append((n, 0))
    count = 0
    visited[n] = 0
    
    while queue:
        now, w = queue.popleft()
        if now == k:
            count += 1
        for i in [-1, 1, now]:
            nxt = now + i
            if 0 <= nxt < MAX:
                if visited[nxt] >= w + 1:
                    visited[nxt] = w + 1
                    queue.append((nxt, w + 1))
                    
    print(visited[k])
    print(count)
            
bfs()