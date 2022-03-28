import sys
from itertools import product
from collections import deque

input = sys.stdin.readline

m, s = map(int, input().split())
fish = [[deque() for _ in range(4)] for _ in range(4)]
smell = [[0] * 4 for _ in range(4)]

# fish direction
fr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
fc = [0, -1, -1, 0, 1, 1, 1, 0, -1]
# shark direction
sr = [0, -1, 0, 1, 0]
sc = [0, 0, -1, 0, 1]

# back tracking direction
bt = list(map(''.join, product(map(str, range(1, 5)), repeat = 3)))

for _ in range(m):
    r, c, d = map(int, input().split())
    fish[r - 1][c - 1].append(d)

# Shark now jaws r, jaws c
jr, jc = map(int, input().split())
jr, jc = jr - 1, jc - 1

def isout(x, y):
    return x >= 4 or y >= 4 or x < 0 or y < 0

def fish_move(before_fish):
    rv = [[deque() for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            for d in before_fish[r][c]:
                nr, nc, nd = r, c, d
                move = 0
                for i in range(8):
                    nd = d - i + 8 if d - i <= 0 else d - i
                    nr = r + fr[nd]
                    nc = c + fc[nd]
                    
                    if isout(nr, nc) or smell[nr][nc]:
                        continue
                    elif jr == nr and jc == nc:
                        continue
                    else: 
                        move = 1
                        break

                if move:
                    rv[nr][nc].append(nd)
                else:
                    rv[r][c].append(d)

    return rv

def eat():
    global jr, jc
    rv = -1
    idx = 0
    for i in range(len(bt)):
        moves = list(map(int, bt[i]))
        visited = [[0] * 4 for _ in range(4)]
        count = 0
        njr, njc = jr, jc
        for move in moves:
            njr += sr[move]
            njc += sc[move]
            if isout(njr, njc):
                count = int(-1e9)
                break
            if visited[njr][njc]:
                continue
            count += len(fish[njr][njc])
            visited[njr][njc] = 1

        if count > rv:
            idx = i
            rv = count
    
    njr, njc = jr, jc
    moves = list(map(int, bt[idx]))
    for i in moves:
        njr += sr[i]
        njc += sc[i]
        if len(fish[njr][njc]):
            smell[njr][njc] = 3
        fish[njr][njc] = deque()
    jr, jc = njr, njc

for _ in range(s):
    clone_fish = [[deque() for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            for i in fish[r][c]:
                clone_fish[r][c].append(i)

    fish = fish_move(fish)
    eat()

    for r in range(4):
        for c in range(4):
            smell[r][c] = max(smell[r][c] - 1, 0)
            for i in clone_fish[r][c]:
                fish[r][c].append(i)

result = sum([len(fish[r][c]) for r in range(4) for c in range(4)])
print(result)