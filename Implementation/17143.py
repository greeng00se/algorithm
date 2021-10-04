import sys

input = sys.stdin.readline

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]

n, m, sc = map(int, input().split())
shark = []
result = 0

for i in range(sc):
    r, c, s, d, z = map(int, input().split())
    shark.append((r, c, s, d, z))
    
fishman = 0
while fishman < m:
    sea = [[0] * (m + 1) for _ in range(n + 1)]
    fishman += 1
    idx = -1
    lowr = int(1e9)
    for i in range(len(shark)):
        if shark[i][1] == fishman and shark[i][0] < lowr:
            lowr = shark[i][0]
            idx = i
                
    if idx != -1:
        result += shark[idx][4]
        shark[idx] = (0, 0, 0, 0, 0)
            
    for i in range(len(shark)):
        r, c, s, d, z = shark[i]
        if r == c == 0:
            continue
        
        while s:
            nr = r + dr[d]
            nc = c + dc[d]
            if 1 <= nr <= n and 1 <= nc <= m:
                r = nr
                c = nc
            else:
                if d in [1, 2]: d ^= 3
                elif d in [3, 4]: d ^= 7
                r = r + dr[d]
                c = c + dc[d]
            s -= 1
                
        shark[i] = (r, c, shark[i][2], d, z)
        if sea[r][c]:
            if shark[sea[r][c] - 1][4] > z:
                shark[i] = (0, 0, 0, 0, 0)
            else:
                shark[sea[r][c] - 1] = (0, 0, 0, 0, 0)
                sea[r][c] = i + 1
        else: sea[r][c] = i + 1
    i = 0
    while len(shark) == i:
        if shark[i][0] == shark[i][1] == 0:
            del shark[i]
        else: i += 1

print(result)