import sys

input = sys.stdin.readline
MAX_GOMOKU = 19

data = [list(map(int, input().split())) for _ in range(MAX_GOMOKU)]
result = 0

dr = [-1, 0, 1, 1]
dc = [1, 1, 1, 0]

def isout(x, y):
    return x < 0 or y < 0 or x >= MAX_GOMOKU or y >= MAX_GOMOKU

def solve():
    for r in range(MAX_GOMOKU):
        for c in range(MAX_GOMOKU):
            if data[r][c] == 0:
                continue

            flag = data[r][c]
            
            for i in range(4):
                count = 0

                br = r - dr[i]
                bc = c - dc[i]
                if not isout(br, bc) and data[br][bc] == flag:
                    continue

                for mul in range(5):
                    nr = r + dr[i] * mul
                    nc = c + dc[i] * mul
                    if isout(nr, nc) or data[nr][nc] != flag:
                        break
                    count += 1
                
                nr = r + dr[i] * 5
                nc = c + dc[i] * 5
                if count == 5 and (isout(nr, nc) or data[nr][nc] != flag):
                    print(flag)
                    print(r + 1, c + 1)
                    return

    print(0)

solve()


            

