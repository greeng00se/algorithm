import sys
from collections import deque

input = sys.stdin.readline

rep = int(input())
queue = deque()
for _ in range(rep):
    op = list(input().split())
    
    if op[0] == 'push_front':
        queue.appendleft(int(op[1]))
    elif op[0] == 'push_back':
        queue.append(int(op[1]))
    elif op[0] == 'pop_front':
        if queue: print(queue.popleft())
        else: print(-1)
    elif op[0] == 'pop_back':
        if queue: print(queue.pop())
        else: print(-1)
    elif op[0] == 'size':
        print(len(queue))
    elif op[0] == 'empty':
        print(0 if queue else 1)
    elif op[0] == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif op[0] == 'back':
        if queue: print(queue[-1])
        else: print(-1)
