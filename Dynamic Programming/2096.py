import sys

input = sys.stdin.readline

n = int(input())

span = [(0, 2), (0, 3), (1, 3)]
dpMin, dpMax = [0] * 3, [0] * 3

for i in range(n):
    data = list(map(int, input().split()))
    tempMin, tempMax = [int(1e9)] * 3, [0] * 3
    for j, s in enumerate(span):
        l, r = s
        tempMin[j] = min(tempMin[j], min(dpMin[l:r]) + data[j])
        tempMax[j] = max(tempMax[j], max(dpMax[l:r]) + data[j])
    dpMin, dpMax = tempMin, tempMax

print(max(dpMax), min(dpMin))
        