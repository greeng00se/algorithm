import sys
from collections import deque

input = sys.stdin.readline

rep = int(input())

dr = [-1, 1, 1, -1]
dc = [1, 1, -1, -1]

def isout(x, y):
    return x > 8 or y > 8 or x <= 0 or y <= 0

def bfs(start, end):
    sr, sc = start
    er, ec = end
    if (sr + sc) % 2 != (er + ec) % 2:
        print('Impossible')
        return
    
    visited = [[int(1e9)] * 9 for i in range(9)]
    visited[sr][sc] = 0
    queue = deque()
    queue.append((sr, sc, []))
    
    while queue:
        step = []
        r, c, move = queue.popleft()
        for m in move: step.append(m)
        step.append((r, c))
        if r == er and c == ec and len(step) <= 3:
            print(len(step) - 1, end = ' ')
            for m in step:
                r, c = m
                print(chr(r + 64), c, end = ' ')
        
        for i in range(4):
            for j in range(1, 8):
                nr = r + (dr[i] * j)
                nc = c + (dc[i] * j)

                if isout(nr, nc):
                    continue
                
                if visited[nr][nc] > len(step):
                    visited[nr][nc] = len(step)
                    queue.append((nr, nc, step))
                
    print()
    
for _ in range(rep):
    ar, ac, br, bc = input().split()
    ar, br = ord(ar) - ord('@'), ord(br) - ord('@')
    ac, bc = int(ac), int(bc)
    bfs((ar, ac), (br, bc))
    
    