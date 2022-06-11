import sys

input = sys.stdin.readline

rep = int(input())

for _ in range(rep):
    n = int(input())
    coins = map(int, input().split())
    k = int(input())
    
    a = [0] * (k + 1)
    a[0] = 1
    for coin in coins:
        for i in range(coin, k + 1):
            a[i] += a[i - coin]
            
    print(a[-1])