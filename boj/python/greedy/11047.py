import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
money = 0
result = 0
for _ in range(n):
    coins.append(int(input()))
    
coins.sort(reverse=True)

for coin in coins:
    v = k // coin
    if v >= 1:
        result += v
        k -= v * coin
        
print(result)