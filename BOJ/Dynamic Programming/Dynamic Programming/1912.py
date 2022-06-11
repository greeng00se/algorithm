n = int(input())
a = list(map(int, input().split()))
dp = [0] * 100001
result = a[0]
dp[0] = a[0]

for i in range(1, n):
    dp[i] = max(a[i], dp[i - 1] + a[i])
    if dp[i] > result:
        result = dp[i]
print(result)