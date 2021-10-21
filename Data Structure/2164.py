import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(1, n + 1):
    queue.append(i)
    
while len(queue) > 1:
    queue.popleft()
    queue.rotate(-1)
    
print(queue.popleft())
    