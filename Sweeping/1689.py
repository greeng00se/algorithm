# 왼쪽 좌표 기준으로 오름차순 정렬
# 힙에 오른쪽 좌표 push
# 현재 왼쪽 좌표 보다 큰 값이 나올 때 까지 힙에서 pop
# 힙의 크기와 현재 결과값과 비교하여 큰 값을 결과값에 저장
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

