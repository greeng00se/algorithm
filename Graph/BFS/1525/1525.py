from collections import defaultdict
from collections import deque

ANSWER = '123456780'
s = ''.join(open(0).read().split())
d = defaultdict(int)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def isout(x, y):
    return x >= 3 or y >= 3 or x < 0 or y < 0

def bfs(s):
    visited = defaultdict(int)

    queue = deque()
    queue.append((s, 0))
    visited[s] = 1
    
    while queue:
        s, now = queue.popleft()
        if s == ANSWER:
            return now

        idx = s.index('0')
        r = idx // 3
        c = idx % 3
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if isout(nr, nc):
                continue
            
            next_idx = nr * 3 + nc
            next_string = list(s)
            next_string[idx], next_string[next_idx] = next_string[next_idx], next_string[idx]
            next_string = ''.join(next_string)

            if visited[next_string]:
                continue
            visited[next_string] = 1
            queue.append((next_string, now + 1))
            
    return -1

print(bfs(s))