import sys
from functools import cmp_to_key

input = sys.stdin.readline

arr = []

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
arr.sort(reverse = True)
for _ in range(k, n):
    arr.append(arr[0])

arr.sort(key = cmp_to_key(lambda x, y : -1 if str(x) + str(y) > str(y) + str(x) else 1))

print(*arr, sep = '')