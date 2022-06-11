import sys
from collections import Counter

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    data = []
    for _ in range(n):
        rank = list(map(int, input().split()))
        data.extend(rank)
        
    point = Counter(data).most_common()
    result = []
    flag = point[1][1]
    for i in range(1, len(point)):
        if point[i][1] == flag:
            result.append(point[i][0])

    print(*sorted(result))
    