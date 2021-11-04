import sys

input = sys.stdin.readline

n, p = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def mul(n, matrixA, matrixB):
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
            result[i][j] %= 1000
    return result

def div(n, matrix, p):
    if p == 1: return matrix
    
    tmp = div(n, matrix, p // 2)
    if p % 2 == 0:
        return mul(n, tmp, tmp)
    else:
        return mul(n, mul(n, tmp, tmp), matrix)
    
result = div(n, matrix, p)
for i in range(n):
    for j in range(n):
        print(result[i][j] % 1000, end=' ')
    print()

