import sys

input = sys.stdin.readline

rep = int(input())

for _ in range(rep):
    n = int(input())
    
    rank = [list(map(int, input().split())) for _ in range(n)]
    rank.sort()

    result = 1
    high = rank[0][1]

    for i in range(1, n):
        if high > rank[i][1]:
            result += 1
            high = rank[i][1]

    print(result)