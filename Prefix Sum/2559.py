import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
psum = [0] * (n + 1)
for i in range(n):
    psum[i + 1] = psum[i] + data[i]

result = int(-1e9)
for i in range(m, n + 1):
    result = max(result, psum[i] - psum[i - m])
print(result)
