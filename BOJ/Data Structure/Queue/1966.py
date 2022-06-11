import sys
from collections import deque

input = sys.stdin.readline

rep = int(input())

for _ in range(rep):
    n, m = map(int, input().split())
    queue = deque()
    weight = list(map(int, input().split()))
    result = 0
    for i, w in enumerate(weight):
        queue.append((i, w))
        
    while queue:
        flag = True
        now = queue[0][1]
        for i in range(1, len(queue)):
            if now < queue[i][1]:
                flag = False
                break
        if flag:
            num = queue.popleft()
            result += 1
            if num[0] == m:
                break
        else: queue.rotate(-1)
    
    print(result)