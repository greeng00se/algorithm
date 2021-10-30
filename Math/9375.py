import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = []
    for i in range(n):
        _, kind = input().split()
        s.append(kind)
    
    r = Counter(s)
    result = 1
    for key in r:
        result *= r[key] + 1
    print(result - 1)