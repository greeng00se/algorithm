import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(input()) for _ in range(n)]
result = 0

for i in range(n):
    flag = 0
    for j in range(m):
        if data[i][j] in '/\\':
            result += 0.5
            flag ^= 1
        if flag and data[i][j] == '.':
            result += 1
            
print(int(result))