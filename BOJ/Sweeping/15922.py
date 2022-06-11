import sys

input = sys.stdin.readline

def solve(data, n):
    result = data[0][1] - data[0][0]
    y = data[0][1]

    for i in range(1, n):
        if y < data[i][1]:
            result += data[i][1] - max(y, data[i][0])
            y = data[i][1]
    
    print(result)

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
solve(data, n)

