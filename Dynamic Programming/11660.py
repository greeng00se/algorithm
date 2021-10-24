n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
query = [list(map(int, input().split())) for _ in range(m)]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + data[i - 1][j - 1]
        
for q in query:
    x1, y1, x2, y2 = q
    print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])
