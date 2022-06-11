import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()
count = Counter(data).most_common(2)
print(round(sum(data) / n))
print(data[n // 2])
if len(count) == 1 or count[0][1] > count[1][1]:
    print(count[0][0])
else:
    print(count[1][0])
print(data[-1] - data[0])