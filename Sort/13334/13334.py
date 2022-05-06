# 사람마다 집과 사무실 위치 오름차순 정렬
# 끝 위치 기준으로 정렬 후 스위핑
# 선분 범위 안에 들어온다면 push
# 선분 범위 밖으로 나간다면 pop
# heapq의 크기 기준으로 사람 수를 구함

import sys
import heapq

input = sys.stdin.readline

def solve(data, d):
    data.sort(key = lambda x: x[1])
    hq = []
    result = 0

    for s, e in data:
        
        if e - d <= s:
            heapq.heappush(hq, s)
        while hq and hq[0] < e - d:
            heapq.heappop(hq)

        result = max(result, len(hq))
        
    return result

n = int(input())
data = [sorted(list(map(int, input().split()))) for _ in range(n)]
d = int(input())

print(solve(data, d))