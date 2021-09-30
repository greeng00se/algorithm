import sys
import math

input = sys.stdin.readline

rep = int(input())
a = []
b = []
for _ in range(rep):
    a.append(int(input()))
    
for i in range(rep - 1):
    b.append(abs(a[i] - a[i + 1]))
    
gcd = b[0]
for i in range(len(b)):
    gcd = math.gcd(gcd, b[i])
    
result = []
for i in range(2, int(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        result.append(i)
        if i * i != gcd:
            result.append(gcd // i)
result.append(gcd)
result.sort()
print(*result)