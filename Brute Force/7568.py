import sys

input = sys.stdin.readline

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]
rank = [1] * n

for i in range(n):
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank[i] += 1
            
print(*rank)
    