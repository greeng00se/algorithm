import sys

input = sys.stdin.readline

n = int(input())

result = 0
for i in range(1, n * 2):
    result += i
    if result > n:
        print(i - 1)
        break
