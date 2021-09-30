import sys
import math

rep = int(input())

for _ in range(rep):
    a, b = map(int, input().split())
    print(a * b // math.gcd(a, b))