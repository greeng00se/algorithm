import sys

input = sys.stdin.readline

def solve(n):
    if n < 100:
        return n
    
    result = 99
    if n >= 1000:
        n = 999
        
    for i in range(100, n + 1):
        hundreds = i // 100
        tens = (i // 10) % 10
        units = i % 10
        if hundreds - tens == tens - units:
            result += 1

    return result

n = int(input())
print(solve(n))