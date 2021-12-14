import sys

input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort(reverse = True)
result = 0

for i in range(n):
    result = max(result, data[i] * (i + 1))

print(result)