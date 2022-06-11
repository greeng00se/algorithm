import sys

input = sys.stdin.readline

n = int(input())
d = [int(input().split()[1]) for _ in range(6)]
r = d.index(max(d))
c = (r + 1) % 6 if d[(r + 1) % 6] > d[r - 1] else r - 1
area = d[r] * d[c] - d[r - 3] * d[c - 3]
print(n * area)
