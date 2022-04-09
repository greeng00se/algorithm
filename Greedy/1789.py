import sys

input = sys.stdin.readline

n = int(input())

result = 0
for i in range(1, n * 2):
    if n == 1: 
        print(1)
        break
    result += i
    if result > n:
        print(i - 1)
        break