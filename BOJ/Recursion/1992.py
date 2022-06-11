import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().rstrip())) for _ in range(n)]
result = ''

def quadtree(r, c, n):
    global result
    flag = 1
    p = data[r][c]
    for i in range(n):
        for j in range(n):
            if data[r + i][c + j] == p:
                continue
            flag = 0
            
    if flag:
        result += str(p)
        return
    
    result += '('
    quadtree(r, c, n // 2)
    quadtree(r, c + n // 2, n // 2)
    quadtree(r + n // 2, c, n // 2)
    quadtree(r + n // 2, c + n // 2, n // 2)
    result += ')'

quadtree(0, 0, n)
print(result)

