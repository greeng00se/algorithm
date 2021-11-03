import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
result = 0

def isNotWall(r, c, d):
    if d == 0 and data[r][c + 1] != 1:
        return True
    if d == 1 and data[r + 1][c] != 1:
        return True
    if d == 2 and data[r + 1][c + 1] != 1 and data[r + 1][c] != 1 and data[r][c + 1] != 1:
        return True
    return False
        
def solve(r, c, d):
    global result
    if r == c == n - 1: result += 1

    if d != 1 and c + 1 < n and isNotWall(r, c, 0):
        solve(r, c + 1, 0)
    if d != 0 and r + 1 < n and isNotWall(r, c, 1):
        solve(r + 1, c, 1)
    if r + 1 < n and c + 1 < n and isNotWall(r, c, 2):
        solve(r + 1, c + 1, 2)
        
if data[n - 1][n - 1] != 1:
    solve(0, 1, 0)
print(result)