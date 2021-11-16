import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
maxCost = sum(cost) + 1
result = 0

dp = [0] * maxCost

for i in range(n):
    tmp = [0] * maxCost
    for j in range(maxCost):
        if j - cost[i] >= 0:
            tmp[j] = max(dp[j], dp[j - cost[i]] + memory[i])
        tmp[j] = max(dp[j], tmp[j])
    dp = tmp
    
for i in range(maxCost):
    if dp[i] >= m:
        result = i
        break
        
print(result)


    
        