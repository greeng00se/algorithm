import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

rep = int(input())

def find(x):
    return bisect_right(data, x) - bisect_left(data, x)

for _ in range(rep):
    n = int(input())
    data = sorted(list(map(int, input().split())))
    m = int(input())
    q = list(map(int, input().split()))
    for i in q:  print(1 if find(i) else 0)
        