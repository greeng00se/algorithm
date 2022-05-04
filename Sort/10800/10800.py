import sys

input = sys.stdin.readline

def solve(balls):
    balls.sort(key = lambda x : x[1])
    
    result = [0] * n
    bsum = [0] * (n + 1)
    sum = 0
    
    idx = 0
    for i in range(n):
        for j in range(idx, n):
            
            if balls[i][1] <= balls[j][1]:
                break

            sum += balls[j][1]
            bsum[balls[j][0]] += balls[j][1]
            idx += 1

        result[balls[i][2]] = sum - bsum[balls[i][0]]

    return result

n = int(input())
balls = []

for i in range(n):
    a, b = map(int, input().split())
    balls.append([a, b, i])

print(*solve(balls), sep = "\n")

