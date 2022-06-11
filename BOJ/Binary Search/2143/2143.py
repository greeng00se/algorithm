import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

def find(data, x):
    return bisect_right(data, x) - bisect_left(data, x)

t = int(input())
n = int(input())
data1 = list(map(int, input().split()))
m = int(input())
data2 = list(map(int, input().split()))

psum1 = []
psum2 = []

for i in range(n):
    psum = data1[i]
    psum1.append(psum)
    for j in range(i + 1, n):
        psum += data1[j]
        psum1.append(psum)

for i in range(m):
    psum = data2[i]
    psum2.append(psum)
    for j in range(i + 1, m):
        psum += data2[j]
        psum2.append(psum)

psum1.sort()
psum2.sort()

result = 0

for i in psum1:
    result += find(psum2, t - i)

print(result)


