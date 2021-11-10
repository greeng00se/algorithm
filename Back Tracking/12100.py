import sys

input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]
def isout(x, y):
    return x >= n or y >= n or x < 0 or y < 0

def move(matrix, d):
    s, e, i = 0, n, 1
    if d in [1, 2]:
        s, e, i = n - 1, -1, -1
        
    isadd = [[False] * n for _ in range(n)]
    result = [[0] * n for _ in range(n)]
    
    for r in range(s, e, i):
        for c in range(s, e, i):
            if matrix[r][c] == 0: continue
            if isadd[r][c]: continue
            nr, nc = r, c
            v = matrix[r][c]
            while True:
                nr += dr[d]
                nc += dc[d]
                if isout(nr, nc): break
                if matrix[nr][nc] == 0: continue
                if matrix[r][c] != matrix[nr][nc]: break
                if matrix[r][c] == matrix[nr][nc]:
                    isadd[r][c], isadd[nr][nc] = True, True
                    v *= 2
                    break
            
            vr, vc = r, c
            while True:
                vr += dr[d ^ 2]
                vc += dc[d ^ 2]
                
                if isout(vr, vc) or result[vr][vc] != 0:
                    vr -= dr[d ^ 2]
                    vc -= dc[d ^ 2]
                    result[vr][vc] = v
                    break
        
    return result
    
def solve(matrix, count):
    global answer
    if count >= 5:
        answer = max(answer, max(map(max, matrix)))
        return
        
    for i in range(4):
        solve(move(matrix, i), count + 1)
        
solve(matrix, 0)
print(answer)