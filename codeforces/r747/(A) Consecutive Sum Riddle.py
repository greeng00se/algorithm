import sys

input = sys.stdin.readline

rep = int(input())

for _ in range(rep):
    n = int(input())
    print(-(n - 1), n)