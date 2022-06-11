import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    data = [list(map(int, input().split()))[::-1] for _ in range(n)]
    data.sort(key = lambda x: (-x[1], -x[0]))
    result = 0
    time = data[0][1]
    
    while time > 0:
        if not data: break
        idx = 0
        x = 0
        for i in range(len(data)):
            if time > data[i][1]:
                break
            if x < data[i][0]:
                x = data[i][0]
                idx = i
        if data[idx][1] >= time:
            result += data[idx][0]
            del data[idx]
        time -= 1
    return result
    
print(solve())