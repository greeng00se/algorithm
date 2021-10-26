n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
query = [list(map(int, input().split())) for _ in range(k)]

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + data[i - 1][j - 1]
        
for q in query:
    x1, y1, x2, y2 = q
    psum = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(psum // ((x2 - x1 + 1) * (y2 - y1 + 1)))
