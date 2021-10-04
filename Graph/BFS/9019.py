import sys
from collections import deque

input = sys.stdin.readline

rep = int(input())

for _ in range(rep):
    a, b = map(int, input().split())
    queue = deque()
    queue.append((a, ''))
    visited = [0] * 10001
    DSLR = ['D', 'S', 'L', 'R']
    
    while queue:
        a, op = queue.popleft()
        
        if a == b:
            print(op)
            break
        
        n = [(a * 2) % 10000, a - 1 if a != 0 else 9999, (a % 1000) * 10 + a // 1000, (a % 10) * 1000 + a // 10]
        for i in range(4):
            if not visited[n[i]]:
                queue.append((n[i], op + DSLR[i]))
                visited[n[i]] = 1