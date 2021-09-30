import sys

input = sys.stdin.readline

a = [list(map(int, input().split())) for _ in range(9)]
zero = [(r, c) for r in range(9) for c in range(9) if not a[r][c]]
flag = False
def solve(r, c):
    num = list(range(10))
    
    for i in range(9):
        num[a[r][i]] = 0
        num[a[i][c]] = 0
            
    nr, nc = r - r % 3, c - c % 3
    for i in range(3):
        for j in range(3):
            num[a[nr + i][nc + j]] = 0
                
    return num

def dfs(x):
    global flag
    if flag:
        return
    if x == len(zero):
        for i in a:
            print(*i)
        flag = True
        return
    
    r, c = zero[x]
    for num in solve(r, c):
        if num:
            a[r][c] = num
            dfs(x + 1)
            a[r][c] = 0
        
dfs(0)
    