import sys

input = sys.stdin.readline

n = int(input())

coord = []
for _ in range(n):
    a, b = map(int, input().split())
    coord.append((a, b))
    
coord.sort()
for c in coord:
    a, b = c
    print(a, b)
    