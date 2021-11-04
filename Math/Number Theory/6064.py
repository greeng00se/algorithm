import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    lcm = m * n // math.gcd(m, n)
    
    result = x
    while True:
        if result >= lcm: result = -1; break
        if (result - y) % n == 0: break
        result += m
        
    print(result)
            
        