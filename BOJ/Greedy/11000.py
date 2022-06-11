import sys
import heapq

input = sys.stdin.readline

def solve():
    data.sort()
    hq = []

    for i in range(n):
        if not hq or hq[0] > data[i][0]:
            heapq.heappush(hq, data[i][1])
        else:
            heapq.heappop(hq)
            heapq.heappush(hq, data[i][1])

    return len(hq)

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
print(solve())