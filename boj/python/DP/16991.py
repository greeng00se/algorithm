import math

n = int(input())

a = [[0] * n for _ in range(n)]
b = []
for _ in range(n):
    x, y = map(int, input().split())
    b.append((x, y))
    
for i in range(n):
    for j in range(n):
        if i == j: continue
        x = (b[j][0] - b[i][0]) ** 2
        y = (b[j][1] - b[i][1]) ** 2
        a[i][j] = math.sqrt(x + y)
    
dp = [[-1] * 65536 for _ in range(17)]

def TSP(cur, flag):
    if flag == (1 << n) - 1:
        if not a[cur][0]:
            return int(1e18)
        return a[cur][0]

    if dp[cur][flag] != -1:
        return dp[cur][flag]
    dp[cur][flag] = int(1e18)
    for i in range(n):
        if flag & (1 << i):
            continue
        if a[cur][i] == 0:
            continue
        dp[cur][flag] = min(dp[cur][flag], TSP(i, flag | (1 << i)) + a[cur][i])
    return dp[cur][flag]
    
print(TSP(0, 1))