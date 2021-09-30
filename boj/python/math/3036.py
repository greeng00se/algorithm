import math

n = int(input())
ring = list(map(int, input().split()))

for i in range(1, n):
    a, b = ring[0], ring[i]
    gcd = math.gcd(a, b)
    print('{0}/{1}'.format(a // gcd, b // gcd))
    