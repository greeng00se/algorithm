import sys
import heapq

input = sys.stdin.readline

def solve(data, n):
    data.sort()
    hq = []
    result = 0

    for i in range(n):
        heapq.heappush(hq, data[i][1])
        while hq and hq[0] <= data[i][0]:
            heapq.heappop(hq)

        result = max(len(hq), result)
    
    print(result)

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
solve(data, n)

