import sys
from collections import deque

input = sys.stdin.readline

m, n, o, p, q, r, s, t, u, v, w = map(int, input().split())
tomato = [[[[[[[[[[list(map(int, input().split())) for _ in range(n)] for _ in range(o)] for _ in range(p)] for _ in range(q)] for _ in range(r)] for _ in range(s)] for _ in range(t)] for _ in range(u)] for _ in range(v)] for _ in range(w)]

tc = 0

for i1 in tomato:
    for i2 in i1:
        for i3 in i2:
            for i4 in i3:
                for i5 in i4:
                    for i6 in i5:
                        for i7 in i6:
                            for i8 in i7:
                                for i9 in i8:
                                    for i10 in i9:
                                        for i11 in i10:
                                            if i11 == 0:
                                                tc += 1

result = 0

d = [[0] * 22 for _ in range(11)]
for i in range(11):
    d[i][i] = 1
    d[i][i + 11] = -1

def isout(i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11):
    a = i1 >= w or i2 >= v or i3 >= u or i4 >= t or i5 >= s or i6 >= r or i7 >= q or i8 >= p or i9 >= o or i10 >= n or i11 >= m
    b = i1 < 0 or i2 < 0 or i3 < 0 or i4 < 0 or i5 < 0 or i6 < 0 or i7 < 0 or i8 < 0 or i9 < 0 or i10 < 0 or i11 < 0
    return a or b

def bfs():
    global tc
    if tc == 0: return 0
    queue = deque()
    result = 0
    for i1 in range(w):
        for i2 in range(v):
            for i3 in range(u):
                for i4 in range(t):
                    for i5 in range(s):
                        for i6 in range(r):
                            for i7 in range(q):
                                for i8 in range(p):
                                    for i9 in range(o):
                                        for i10 in range(n):
                                            for i11 in range(m):
                                                if tomato[i1][i2][i3][i4][i5][i6][i7][i8][i9][i10][i11] <= 0: continue
                                                queue.append((i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, 0))
                
    while queue:
        i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, c = queue.popleft()
        result = max(result, c)
        for i in range(22):
            ni1, ni2, ni3, ni4, ni5, ni6, ni7, ni8, ni9, ni10, ni11 = i1 + d[0][i], i2 + d[1][i], i3 + d[2][i], i4 + d[3][i], i5 + d[4][i], i6 + d[5][i], i7 + d[6][i], i8 + d[7][i], i9 + d[8][i], i10 + d[9][i], i11 + d[10][i]
            if isout(ni1, ni2, ni3, ni4, ni5, ni6, ni7, ni8, ni9, ni10, ni11): continue
            if tomato[ni1][ni2][ni3][ni4][ni5][ni6][ni7][ni8][ni9][ni10][ni11] == 0:
                tomato[ni1][ni2][ni3][ni4][ni5][ni6][ni7][ni8][ni9][ni10][ni11] = 1
                queue.append((ni1, ni2, ni3, ni4, ni5, ni6, ni7, ni8, ni9, ni10, ni11, c + 1))
                tc -= 1

    if tc != 0: return -1
    return result

print(bfs())
        
    
