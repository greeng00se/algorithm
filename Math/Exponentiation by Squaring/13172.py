import sys
import math
input = sys.stdin.readline

MOD = int(1e9) + 7
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

def mul(k, p):
    if p == 1: return k % MOD
    tmp = mul(k, p // 2)
    if p % 2 == 0:
        return (tmp * tmp) % MOD
    else:
        return (tmp * tmp * k) % MOD

u, d = data[0][1], data[0][0]
for i in range(1, n):
    u = u * data[i][0] + d * data[i][1]
    d = d * data[i][0]

print(u * mul(d, MOD - 2) % MOD)