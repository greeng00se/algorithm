import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    data = list(map(int, input().split()))

    if sum(data) != (n * (n - 1)) // 2:
        return -1
    
    data.sort(reverse = True)
    if data[-1] == data[-2] == 0: return -1
    v, w = n - 1, 1
    for score in data:
        if score > v:
            return -1
        while score < v:
            v -= 1
            w += 2
        if score == v:
            w -= 1
            if not w:
                v -= 1
                w = 1
            
    return 1
    
print(solve())

