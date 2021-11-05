import sys

input = sys.stdin.readline

rep = int(input())

for _ in range(rep):
    a, b, c = map(int, input().split())
    result = [0, 0, 0]
    if a <= max(b, c):
        result[0] = max(b, c) + 1
    if b <= max(a, c):
        result[1] = max(a, c) + 1
    if c <= max(a, b):
        result[2] = max(a, b) + 1

    if result[0]: result[0] = result[0] - a
    if result[1]: result[1] = result[1] - b
    if result[2]: result[2] = result[2] - c
        
    print(*result)