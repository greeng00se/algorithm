import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key = lambda x : (x[1], x[0]))
for i in data:
    print(*i)