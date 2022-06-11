import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]

dp = [INF] * (n + 100)
dp[0] = 0

for cost, customer in data:
    for i in range(1, n + 100):
        dp[i] = min(dp[i - customer] + cost, dp[i])

print(min(dp[n:]))