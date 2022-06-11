import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
psum = [0] * (n + 1)

for i in range(n):
    psum[i + 1] = psum[i] + data[i]

result = []
for i in range(m, n + 1):
    result.append(psum[i] - psum[i - m])

result.sort(reverse = True)

if result[0]:
    print(result[0])
    print(result.count(result[0]))
else:
    print('SAD')