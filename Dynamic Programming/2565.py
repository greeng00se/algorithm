import sys

input = sys.stdin.readline

n = int(input())
lines = []
dp = [0] * 101

for _ in range(n):
    a, b = map(int, input().split())
    lines.append([a, b])
    
lines.sort()

for i in range(1, n + 1):
    s = 0
    for j in range(1, i):
        if lines[i - 1][1] > lines[j - 1][1] and dp[j] > dp[s]:
            s = j
    dp[i] = dp[s] + 1
    
print(n - max(dp))