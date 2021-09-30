x = int(input())
p = x

dp = [int(1e9)] * 1000001
dp[x] = 0
prev = [0] * 1000001

while True:
    if x == 1: break
    if x % 3 == 0 and dp[x // 3] > dp[x] + 1:
        dp[x // 3] = dp[x] + 1
        prev[x // 3] = x
    if x % 2 == 0 and dp[x // 2] > dp[x] + 1:
        dp[x // 2] = dp[x] + 1
        prev[x // 2] = x
    if dp[x - 1] > dp[x] + 1:
        dp[x - 1] = dp[x] + 1
        prev[x - 1] = x
    x -= 1

print(dp[1])
result = []
n = 1
while True:
    result.append(n)
    if n == p:
        break
    n = prev[n]
    
print(*reversed(result))
    
    