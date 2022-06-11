import sys

input = sys.stdin.readline

n = int(input())

data = [[] for _ in range(201)]
for i in range(n):
    a, b = input().split()
    a = int(a)
    data[a].append(b)

for i in range(201):
    for v in data[i]:
        print(i, v)
    