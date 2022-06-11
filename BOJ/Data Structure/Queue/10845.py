import sys
from collections import deque

input = sys.stdin.readline

rep = int(input())
queue = deque()
for _ in range(rep):
    op = list(input().split())
    
    if op[0] == 'push':
        queue.append(int(op[1]))
    if op[0] == 'pop':
        if queue: print(queue.popleft())
        else: print(-1)
    if op[0] == 'size':
        print(len(queue))
    if op[0] == 'empty':
        print(0 if queue else 1)
    if op[0] == 'front':
        if queue: print(queue[0])
        else: print(-1)
    if op[0] == 'back':
        if queue: print(queue[-1])
        else: print(-1)