import sys
from collections import defaultdict

input = sys.stdin.readline

def solve():
    n = int(input())
    data = [input().rstrip() for _ in range(n)]
    data.sort()

    d = defaultdict(int)

    for i in range(n):

        for j in range(1, len(data[i]) + 1):
            if d[data[i][:j]] != 0:
                return 'NO'
        
        d[data[i]] = 1

    return 'YES'

t = int(input())
for i in range(t):
    print(solve())

