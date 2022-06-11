n = int(input())

def solve(n):
    dp = [0] * 1001
    dp[1], dp[2] = 1, 3
    if n <= 2: return dp[n]

    for i in range(3, n + 1):
        dp[i] = dp[i - 2] * 2 + dp[i - 1]
    
    return dp[n]
    
print(solve(n) % 10007)