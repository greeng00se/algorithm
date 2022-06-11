import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

wdr = [0, [-1, 0, 1], [-1, 0, 1], [-1, -1, -1], [1, 1, 1]]
wdc = [0, [1, 1, 1], [-1, -1, -1], [-1, 0, 1], [-1, 0, 1]]

def isout(r, c):
    return r < 0 or c < 0 or r >= x or c >= y

def isvalid(r, c, d, i):
    nr = r + wdr[d][i]
    nc = c + wdc[d][i]

    if i == 1 and (nr, nc) in wall[(r, c)]:
        return 1

    if dr[d] == 0 and ((nr, c) in wall[(r, c)] or (nr, c) in wall[(nr, nc)]):
        return 1

    if dc[d] == 0 and ((r, nc) in wall[(r, c)] or (r, nc) in wall[(nr, nc)]):
        return 1

    return 0
        
# 집에 있는 모든 온풍기에서 바람이 한 번 나옴
def step1():
    for heater in heaters:
        r, c, d = heater
        
        nr = r + dr[d]
        nc = c + dc[d]

        visited = [[0] * y for _ in range(x)]
        queue = deque()

        queue.append((nr, nc, 5))
        wind[nr][nc] += 5
        visited[nr][nc] = 1

        while queue:
            r, c, v = queue.popleft()

            if v == 1: 
                continue

            for i in range(3):
                nr = r + wdr[d][i]
                nc = c + wdc[d][i]

                if isout(nr, nc): 
                    continue

                if isvalid(r, c, d, i):
                    continue

                if visited[nr][nc]:
                    continue

                visited[nr][nc] = 1
                wind[nr][nc] += v - 1
                queue.append((nr, nc, v - 1))

    return

# 온도가 조절됨
def step2():
    newwind = [[0] * y for _ in range(x)]

    for r in range(x):
        for c in range(y):
            for i in range(1, 5):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if isout(nr, nc):
                    continue

                if wind[nr][nc] > wind[r][c]:
                    continue

                if (r, c) in wall[(nr, nc)]:
                    continue

                diff = (wind[r][c] - wind[nr][nc]) // 4
                newwind[nr][nc] += diff
                newwind[r][c] -= diff
            
            newwind[r][c] += wind[r][c]

    return newwind

# 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
def step3():
    for r in range(x):
        for c in range(y):
            if r == 0 or c == 0 or r == x - 1 or c == y - 1:
                wind[r][c] = max(0, wind[r][c] - 1)

# 초콜릿을 하나 먹는다.

# 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.
def step4():
    result = len(checkers)
    for checker in checkers:
        r, c = checker
        if wind[r][c] >= k:
            result -= 1

    return 0 if result else 1
        
x, y, k = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(x)]
w = int(input())
wall = defaultdict(list)
for _ in range(w):
    r, c, t = map(int, input().split())
    r, c = r - 1, c - 1
    wall[(r, c)].append((r - 1, c) if t == 0 else (r, c + 1))
    wall[(r - 1, c) if t == 0 else (r, c + 1)].append((r, c))

heaters = []
checkers = []
for r in range(x):
    for c in range(y):
        if data[r][c] == 0:
            continue
        if data[r][c] == 5:
            checkers.append((r, c))
            continue
        heaters.append((r, c, data[r][c]))

wind = [[0] * y for _ in range(x)]
result = 0

while result <= 100:
    step1()
    wind = step2()
    step3()

    result += 1
    if step4():
        break

print(result)

