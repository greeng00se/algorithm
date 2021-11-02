# nCr = n!/(n-r)!r!

dp = [1] * 31
for i in range(1, 31):
    dp[i] = dp[i - 1] * i
    
rep = int(input())
for _ in range(rep):
    m, n = map(int, input().split())
    print(dp[n] // dp[n - m] // dp[m])