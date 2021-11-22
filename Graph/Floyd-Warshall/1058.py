import sys

input = sys.stdin.readline

n = int(input())
data = [list(input()) for _ in range(n)]
v = [[0] * n for _ in range(n)]
result = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b: continue
            if data[a][b] == 'Y' or data[a][k] == data[k][b] == 'Y':
                v[a][b] = 1
                
for i in range(n):
    result = max(result, sum(v[i]))
                
print(result)