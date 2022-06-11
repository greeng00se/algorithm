import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    data = [tuple(map(int, input().split())) for _ in range(n)]
    s = set(data)
    result = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            x1, y1 = data[i]
            x2, y2 = data[j]
            dx, dy = x1 - x2, y1 - y2

            if (x1 - dy, y1 + dx) in s and (x2 - dy, y2 + dx) in s:
                result = max(result, dx * dx + dy * dy)

    print(result)


