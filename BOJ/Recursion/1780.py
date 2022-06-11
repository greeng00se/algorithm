import sys

input = sys.stdin.readline

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

def check(r, c, k):
    flag = data[r][c]
    for i in range(k):
        for j in range(k):
            if flag == data[r + i][c + j]: continue
            return False
        
    return True

result = [0, 0, 0]
def solve(r, c, k):
    if k == 1:
        result[data[r][c] + 1] += 1
        return 
    
    if check(r, c, k):
        result[data[r][c] + 1] += 1
        return
    
    for i in range(0, k, k // 3):
        for j in range(0, k, k // 3):
            solve(r + i, c + j, k // 3)
            
solve(0, 0, n)
for r in result:
    print(r)
        