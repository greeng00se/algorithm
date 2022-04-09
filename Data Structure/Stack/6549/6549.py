import sys
from collections import deque

input = sys.stdin.readline

while True:
    data = list(map(int, input().split())) + [0]
    if data[0] == 0:
        break

    result = 0
    stack = deque()
    print(data)

    for i in range(1, len(data)):
        while stack and data[stack[-1]] > data[i]:
            idx = stack.pop()
            if stack:
                result = max(result, (i - stack[-1] - 1) * data[idx])
            else:
                result = max(result, (i - 1) * data[idx])
        stack.append(i)

    print(result)
