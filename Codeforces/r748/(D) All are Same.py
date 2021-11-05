import sys
import math
 
input = sys.stdin.readline
 
rep = int(input())

for _ in range(rep):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    a = data[1] - data[0]
    b = data[2] - data[0]
    g = math.gcd(a, b)
    for i in range(3, n):
        b = data[i] - data[0]
        g = math.gcd(g, b)
    
    if g <= 0: print(-1)
    else: print(g)