import sys
from bisect import bisect_left
input = sys.stdin.readline

rep = int(input())

for _ in range(rep):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()
    i = m - 1
    result = 0
    cat = 0
    while cat < n and i >= 0:
        mouse = data[i]
        if cat >= mouse: break
        cat += n - mouse
        if cat > n: break
        result += 1            
        i -= 1
    print(result)