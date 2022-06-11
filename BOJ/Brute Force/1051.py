import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(input()) for _ in range(n)]
result = 1

for i in range(1, min(m, n)):
    for j in range(n - i):
        for k in range(m - i):
            if data[j][k] == data[j + i][k] == data[j][k + i] == data[j + i][k + i]:
                if (i + 1) * (i + 1) > result:
                    result = (i + 1) * (i + 1)
                    
print(result)
            