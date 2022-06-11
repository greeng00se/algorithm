import sys

input = sys.stdin.readline

def getChickenDistance(indexs):
    global answer
    
    result = 0

    for hr, hc in house:
        minDistance = int(1e9)
    
        for i in indexs:
            r, c = chicken[i]        
            minDistance = min(minDistance, abs(r - hr) + abs(c - hc))  

        result += minDistance

    answer = min(answer, result)

def solve(indexs, depth, start):

    if depth == m:
        getChickenDistance(indexs)
        return

    for i in range(start, len(chicken)):
        if usedIndexs[i]: 
            continue
        usedIndexs[i] = 1
        indexs[depth] = i
        solve(indexs, depth + 1, i + 1)
        usedIndexs[i] = 0

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
house = [(r, c) for r in range(n) for c in range(n) if data[r][c] == 1]
chicken = [(r, c) for r in range(n) for c in range(n) if data[r][c] == 2]
usedIndexs = [0] * len(chicken)
answer = int(1e9)
solve([0] * m, 0, 0)
print(answer)