n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
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