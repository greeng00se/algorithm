import sys

input = sys.stdin.readline

n = int(input())
data = list(input().rstrip())
MOD = 1234567891
result = 0

for i in range(n):
    result += (ord(data[i]) - 96) * (31 ** i)
    
print(result % MOD)
