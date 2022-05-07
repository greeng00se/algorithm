import sys

input = sys.stdin.readline

def solve(data, n):
    data.sort()
    result = 1
    highRank = data[0][1]

    for i in range(1, n):
        if highRank > data[i][1]:
            highRank = data[i][1]
            result += 1
    
    print(result)

t = int(input())
for _ in range(t):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    solve(data, n)
